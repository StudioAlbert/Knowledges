// Génère le site statique des supports de cours à partir du vault Obsidian.
//
//   01 courses/slides/<catégorie>/*.md     → decks reveal.js (format Advanced Slides)
//   01 courses/exercises/<catégorie>/*.md  → pages HTML
//
// Tout dossier dont le nom commence par `_` est ignoré (_archives_to_cut, _drafts…).
// Sortie : site-build/dist/, déployée telle quelle sur le VPS.

import fs from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import matter from 'gray-matter';
import MarkdownIt from 'markdown-it';
import hljs from 'highlight.js';

const HERE = import.meta.dirname;
const ROOT = path.resolve(HERE, '..');
const COURSES = path.join(ROOT, '01 courses');
const IMAGES = path.join(ROOT, '00 images');
const CSS = path.join(ROOT, '00 templates', 'css');
const REVEAL = path.join(HERE, 'node_modules', 'reveal.js');
const DIST = path.join(HERE, 'dist');

const KINDS = [
  { dir: 'slides', label: 'Slides', urlSegment: 'slides' },
  { dir: 'exercises', label: 'Exercices', urlSegment: 'exercices' },
];

const IMAGE_EXT = /\.(png|jpe?g|gif|svg|webp|avif)$/i;

// ---------------------------------------------------------------------------
// Utilitaires

const escapeHtml = (s) =>
  String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);

const slugify = (s) =>
  s
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/\+\+/g, 'pp')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');

const byName = (a, b) => a.name.localeCompare(b.name, 'fr', { numeric: true });

const encodePath = (p) => p.split('/').map(encodeURIComponent).join('/');

async function walk(dir, filter) {
  const out = [];
  for (const entry of await fs.readdir(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('_') || entry.name.startsWith('.')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...(await walk(full, filter)));
    else if (filter(entry.name)) out.push(full);
  }
  return out;
}

async function writeFile(file, content) {
  await fs.mkdir(path.dirname(file), { recursive: true });
  await fs.writeFile(file, content);
}

// Applique `fn` à chaque ligne hors blocs de code délimités (``` ou ~~~).
function mapOutsideFences(text, fn) {
  let fence = null;
  return text
    .split(/\r?\n/)
    .map((line) => {
      const m = line.match(/^\s*(`{3,}|~{3,})/);
      if (m) {
        if (!fence) fence = m[1][0];
        else if (m[1][0] === fence) fence = null;
        return line;
      }
      return fence ? line : fn(line);
    })
    .join('\n');
}

// ---------------------------------------------------------------------------
// Collecte

async function collect() {
  const items = [];
  for (const kind of KINDS) {
    const kindDir = path.join(COURSES, kind.dir);
    for (const cat of await fs.readdir(kindDir, { withFileTypes: true })) {
      if (!cat.isDirectory() || cat.name.startsWith('_')) continue;
      for (const file of await walk(path.join(kindDir, cat.name), (n) => n.endsWith('.md'))) {
        const { data, content } = matter(await fs.readFile(file, 'utf8'));
        const name = path.basename(file, '.md');
        const h1 = content.match(/^#\s+(.+)$/m)?.[1];
        const slug = slugify(name);
        items.push({
          kind,
          category: cat.name,
          file,
          dir: path.dirname(file),
          name,
          code: name.match(/^[A-Z]+-[A-Z]+-[A-Z]+-\d+/)?.[0] ?? null,
          title: data.title ?? h1 ?? name,
          fm: data,
          body: content,
          url: `/${slugify(cat.name)}/${kind.urlSegment}/${slug}/`,
          out: path.join(DIST, slugify(cat.name), kind.urlSegment, slug),
        });
      }
    }
  }
  return items;
}

// ---------------------------------------------------------------------------
// Résolution des liens et images Obsidian

class Resolver {
  constructor(items, imageIndex) {
    this.byName = new Map(items.map((it) => [it.name.toLowerCase(), it]));
    this.imageIndex = imageIndex; // nom de fichier → chemin dans 00 images
    this.copies = new Map(); // destination → source
  }

  // Renvoie l'URL publique d'une image référencée depuis `item`, ou null.
  image(item, ref) {
    const clean = decodeURIComponent(ref.split('|')[0].trim());
    const base = path.basename(clean);
    const local = path.resolve(item.dir, clean);
    if (existsSync(local) && !local.startsWith(IMAGES)) {
      const dest = path.join(item.out, clean);
      this.copies.set(dest, local);
      return encodePath(clean.replace(/\\/g, '/'));
    }
    if (this.imageIndex.has(base)) return '/assets/images/' + encodeURIComponent(base);
    console.warn(`  ⚠ image introuvable dans ${item.name} : ${ref}`);
    return null;
  }

  // Réécrit la syntaxe Obsidian d'une ligne en Markdown standard.
  line(item, line) {
    return line
      .replace(/(["'(])00 images\//g, '$1/assets/images/')
      .replace(/!\[\[([^\]]+)\]\]/g, (all, ref) => {
        if (!IMAGE_EXT.test(ref.split('|')[0])) return '';
        const url = this.image(item, ref);
        return url ? `![](${url})` : '';
      })
      .replace(/!\[([^\]]*)\]\((?!https?:|data:|\/)([^)\s]+)\)/g, (all, alt, src) => {
        const url = this.image(item, src);
        return url ? `![${alt}](${url})` : all;
      })
      .replace(/\[\[([^\]]+)\]\]/g, (all, inner) => {
        const [target, alias] = inner.split('|');
        const label = alias ?? target.split('#')[0];
        const hit = this.byName.get(path.basename(target.split('#')[0]).trim().toLowerCase());
        return hit ? `[${label}](${hit.url})` : label;
      });
  }

  markdown(item, text) {
    return mapOutsideFences(text, (l) => this.line(item, l));
  }
}

// ---------------------------------------------------------------------------
// Slides

// Découpe sur les lignes `---` hors code et retire les notes orateur (`Note:` → fin de diapo).
function splitSlides(body) {
  const slides = [[]];
  let fence = null;
  let inNotes = false;
  for (const line of body.split(/\r?\n/)) {
    const m = line.match(/^\s*(`{3,}|~{3,})/);
    if (m) {
      if (!fence) fence = m[1][0];
      else if (m[1][0] === fence) fence = null;
    } else if (!fence && line.trim() === '---') {
      slides.push([]);
      inNotes = false;
      continue;
    } else if (!fence && /^notes?:/i.test(line)) {
      inNotes = true;
    }
    if (!inNotes) slides.at(-1).push(line);
  }
  return slides.map((s) => s.join('\n').trim()).filter(Boolean);
}

async function renderDeck(item, resolver, themes) {
  const theme = themes.has(item.fm.theme) ? item.fm.theme : 'white';
  const css = [item.fm.css ?? []].flat().map((c) => '/assets/css/' + encodeURIComponent(path.basename(c)));
  const sections = splitSlides(resolver.markdown(item, item.body))
    .map((md) => `<section data-markdown><textarea data-template>\n${md.replace(/&/g, '&amp;').replace(/</g, '&lt;')}\n</textarea></section>`)
    .join('\n');
  const options = {
    hash: true,
    slideNumber: item.fm.slideNumber ?? true,
    transition: item.fm.transition ?? 'slide',
    width: item.fm.width ?? 960,
    height: item.fm.height ?? 700,
  };

  const html = `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escapeHtml(item.title)}</title>
<link rel="stylesheet" href="/assets/reveal/dist/reset.css">
<link rel="stylesheet" href="/assets/reveal/dist/reveal.css">
<link rel="stylesheet" href="/assets/reveal/dist/theme/${theme}.css">
<link rel="stylesheet" href="/assets/reveal/plugin/highlight/monokai.css">
${css.map((href) => `<link rel="stylesheet" href="${href}">`).join('\n')}
<style>.deck-home{position:fixed;top:10px;left:12px;z-index:30;font:13px system-ui,sans-serif;color:#888;text-decoration:none}.deck-home:hover{color:#E30613}</style>
</head>
<body>
<a class="deck-home" href="/">← Supports</a>
<div class="reveal"><div class="slides">
${sections}
</div></div>
<script src="/assets/reveal/dist/reveal.js"></script>
<script src="/assets/reveal/plugin/markdown/markdown.js"></script>
<script src="/assets/reveal/plugin/highlight/highlight.js"></script>
<script>Reveal.initialize(Object.assign(${JSON.stringify(options)}, { plugins: [RevealMarkdown, RevealHighlight] }));</script>
</body>
</html>
`;
  await writeFile(path.join(item.out, 'index.html'), html);
}

// ---------------------------------------------------------------------------
// Pages Markdown (exercices)

const md = new MarkdownIt({
  html: true,
  linkify: true,
  highlight(code, lang) {
    if (lang && hljs.getLanguage(lang)) {
      return `<pre class="hljs"><code>${hljs.highlight(code, { language: lang, ignoreIllegals: true }).value}</code></pre>`;
    }
    return '';
  },
});

// Callouts Obsidian : `> [!type] …` → <blockquote class="callout" data-callout="type">
md.core.ruler.push('obsidian_callouts', (state) => {
  const tokens = state.tokens;
  for (let i = 0; i < tokens.length - 2; i++) {
    if (tokens[i].type !== 'blockquote_open' || tokens[i + 2].type !== 'inline') continue;
    const first = tokens[i + 2].children?.[0];
    const m = first?.type === 'text' && first.content.match(/^\[!(\w+)\][+-]?[ \t]*/);
    if (!m) continue;
    first.content = first.content.slice(m[0].length);
    tokens[i].attrJoin('class', 'callout');
    tokens[i].attrSet('data-callout', m[1].toLowerCase());
  }
});

function pageShell(title, body, { crumbs = '' } = {}) {
  return `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escapeHtml(title)}</title>
<link rel="stylesheet" href="/assets/hljs.css">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="topbar"><a href="/">Supports de cours</a>${crumbs}</header>
<main>
${body}
</main>
</body>
</html>
`;
}

async function renderPage(item, resolver) {
  const html = md.render(resolver.markdown(item, item.body));
  const crumbs = ` <span>›</span> ${escapeHtml(item.category)} <span>›</span> ${item.kind.label}`;
  await writeFile(path.join(item.out, 'index.html'), pageShell(item.title, `<article>\n${html}</article>`, { crumbs }));
}

// ---------------------------------------------------------------------------
// Accueil

async function renderIndex(items) {
  const categories = [...new Set(items.map((it) => it.category))].sort((a, b) => a.localeCompare(b, 'fr'));
  const blocks = categories.map((cat) => {
    const columns = KINDS.map((kind) => {
      const list = items.filter((it) => it.category === cat && it.kind === kind).sort(byName);
      if (!list.length) return '';
      const lis = list
        .map((it) => {
          const code = it.code ? `<span class="code">${escapeHtml(it.code)}</span>` : '';
          return `<li><a href="${it.url}">${code}${escapeHtml(it.title)}</a></li>`;
        })
        .join('\n');
      return `<div class="column"><h3>${kind.label} <small>${list.length}</small></h3><ul>\n${lis}\n</ul></div>`;
    }).join('\n');
    return `<section class="category"><h2>${escapeHtml(cat)}</h2><div class="columns">${columns}</div></section>`;
  });
  const body = `<h1>Supports de cours</h1>\n<p class="lead">SAE Institute Genève — Games Programming</p>\n${blocks.join('\n')}`;
  await writeFile(path.join(DIST, 'index.html'), pageShell('Supports de cours', body));
}

// ---------------------------------------------------------------------------
// Assets

async function copyAssets(resolver) {
  await fs.cp(path.join(REVEAL, 'dist'), path.join(DIST, 'assets/reveal/dist'), { recursive: true });
  await fs.cp(path.join(REVEAL, 'plugin'), path.join(DIST, 'assets/reveal/plugin'), { recursive: true });
  await fs.cp(IMAGES, path.join(DIST, 'assets/images'), { recursive: true });
  await fs.copyFile(path.join(HERE, 'assets/site.css'), path.join(DIST, 'assets/site.css'));
  await fs.copyFile(path.join(HERE, 'node_modules/highlight.js/styles/github.min.css'), path.join(DIST, 'assets/hljs.css'));

  // Les CSS du vault pointent vers `../../00 images/` (relatif à 00 templates/css/).
  for (const name of await fs.readdir(CSS)) {
    const css = (await fs.readFile(path.join(CSS, name), 'utf8')).replaceAll('../../00 images/', '../images/');
    await writeFile(path.join(DIST, 'assets/css', name), css);
  }

  for (const [dest, src] of resolver.copies) {
    await fs.mkdir(path.dirname(dest), { recursive: true });
    await fs.copyFile(src, dest);
  }
}

// ---------------------------------------------------------------------------

async function main() {
  await fs.rm(DIST, { recursive: true, force: true });

  const items = await collect();
  const imageIndex = new Map((await walk(IMAGES, (n) => IMAGE_EXT.test(n))).map((p) => [path.basename(p), p]));
  const themes = new Set(
    (await fs.readdir(path.join(REVEAL, 'dist/theme'))).filter((f) => f.endsWith('.css')).map((f) => f.slice(0, -4)),
  );
  const resolver = new Resolver(items, imageIndex);

  for (const item of items) {
    console.log(`${item.kind.label.padEnd(9)} ${item.category} / ${item.name}`);
    if (item.kind.dir === 'slides') await renderDeck(item, resolver, themes);
    else await renderPage(item, resolver);
  }
  await renderIndex(items);
  await copyAssets(resolver);

  console.log(`\n${items.length} documents → ${path.relative(ROOT, DIST)}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
