// Génère le site statique des supports de cours à partir du vault Obsidian.
//
//   01 courses/slides/<catégorie>/<CODE> - *.md  → deck reveal.js (format Advanced Slides)
//   01 courses/exercises/<catégorie>/*.md        → onglet Exercices de la séance
//   01 courses/resources/<catégorie>/*.md        → onglet Ressources de la séance
//
// Le site est organisé par séance (code GPR-CF-BDP-01…). Une séance n'est publiée
// que si le frontmatter de ses slides porte `publish: true`. Un exercice ou une
// ressource s'y rattache par `seances: [CODE, …]` ou par un nom commençant par le code.
// Rien d'autre n'est publié.
//
// Fiche GitHub : dans un exercice ou une ressource, un bloc délimité `github`
// insère l'en-tête du dépôt et son README, récupérés au build (repli sur un clone
// local sous `01 courses/companion projects/`). Contenu : `owner/name` ou une URL,
// ou des lignes `repo:` / `ref:` (branche ou tag) / `readme: false`.
// GITHUB_TOKEN facultatif (limite de 60 requêtes/h sans jeton).
//
// Tout dossier dont le nom commence par `_` est ignoré (_archives_to_cut, _drafts…).
// Sortie : site-build/dist/, déployée telle quelle sur le VPS.

import fs from 'node:fs/promises';
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
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
const COMPANIONS = path.join(COURSES, 'companion projects');

const KINDS = [
  { dir: 'slides', label: 'Slides', urlSegment: 'slides' },
  { dir: 'exercises', label: 'Exercices', urlSegment: 'exercices' },
  { dir: 'resources', label: 'Ressources', urlSegment: 'ressources' },
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
          url: null, // fixés par buildSeances pour les documents publiés
          out: null,
        });
      }
    }
  }
  return items;
}

// Regroupe les documents par séance active et fixe leurs URLs de sortie.
function buildSeances(items) {
  const seances = new Map();
  for (const deck of items.filter((it) => it.kind.dir === 'slides' && it.code).sort(byName)) {
    if (deck.fm.publish !== true) continue;
    const slug = slugify(deck.code);
    const url = `/${slugify(deck.category)}/${slug}/`;
    const out = path.join(DIST, slugify(deck.category), slug);
    Object.assign(deck, { url: url + 'slides/', out: path.join(out, 'slides') });
    seances.set(deck.code, { code: deck.code, category: deck.category, title: deck.title, url, out, deck, exercises: [], resources: [] });
  }

  const known = new Set(items.map((it) => it.code).filter(Boolean));
  for (const item of items.filter((it) => it.kind.dir !== 'slides').sort(byName)) {
    const codes = new Set([...[item.fm.seances ?? []].flat().map(String), ...(item.code ? [item.code] : [])]);
    for (const code of codes) {
      const seance = seances.get(code);
      if (!seance) {
        if (!known.has(code)) console.warn(`  ⚠ ${item.name} : séance inconnue ${code}`);
        continue;
      }
      (item.kind.dir === 'exercises' ? seance.exercises : seance.resources).push(item);
      // Un document partagé entre séances est rendu dans chacune ; ses liens pointent vers la première.
      if (!item.url) Object.assign(item, { url: `${seance.url}#${item.kind.urlSegment}`, out: seance.out });
    }
  }

  for (const s of seances.values()) {
    if (!s.exercises.length) console.warn(`  ⚠ ${s.code} : aucun exercice rattaché`);
  }
  return [...seances.values()];
}

// ---------------------------------------------------------------------------
// Résolution des liens et images Obsidian

class Resolver {
  // `items` : documents publiés uniquement ; un lien vers autre chose devient du texte.
  constructor(items, imageIndex) {
    this.byName = new Map(items.map((it) => [it.name.toLowerCase(), it]));
    // Chemin vault sans extension : départage un deck et un exercice de même nom.
    const vaultPath = (it) => path.relative(ROOT, it.file).replace(/\\/g, '/').replace(/\.md$/, '').toLowerCase();
    this.byPath = new Map(items.map((it) => [vaultPath(it), it]));
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
      // Absolue : le document peut être rendu dans une autre page que son dossier de sortie.
      return '/' + encodePath(path.relative(DIST, dest).replace(/\\/g, '/'));
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
        const label = alias ?? path.basename(target.split('#')[0]);
        const key = target.split('#')[0].trim().toLowerCase();
        const hit = this.byPath.get(key) ?? this.byName.get(path.basename(key));
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

async function renderDeck(seance, resolver, themes) {
  const item = seance.deck;
  const theme = themes.has(item.fm.theme) ? item.fm.theme : 'white';
  const css = [item.fm.css ?? []].flat().map((c) => {
    const name = path.basename(c);
    return versioned('/assets/css/' + encodeURIComponent(name), path.join(CSS, name));
  });
  const sections = splitSlides(resolver.markdown(item, item.body))
    .map((md) => `<section data-markdown><textarea data-template>\n${md.replace(/&/g, '&amp;').replace(/</g, '&lt;')}\n</textarea></section>`)
    .join('\n');
  const options = {
    hash: true,
    slideNumber: item.fm.slideNumber ?? true,
    transition: item.fm.transition ?? 'slide',
    // 16:9 sans marge : les fonds 1920×1080 (contain) épousent le cadre de la slide.
    width: item.fm.width ?? 1280,
    height: item.fm.height ?? 720,
    margin: item.fm.margin ?? 0,
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
<a class="deck-home" href="${seance.url}" target="_top">← ${escapeHtml(seance.code)}</a>
<script>if (window.self !== window.top) document.querySelector('.deck-home').hidden = true;</script>
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

// ---------------------------------------------------------------------------
// Fiches GitHub (blocs ```github)

const GITHUB_FENCE = /^[ \t]*(`{3,}|~{3,})github[ \t]*\r?\n([\s\S]*?)^[ \t]*\1[ \t]*$/gm;
const repos = new Map(); // clé owner/name@ref → { info, readme, ref }

function parseGithubBlock(text) {
  const spec = { repo: null, ref: null, readme: true };
  for (const raw of text.split(/\r?\n/)) {
    const line = raw.replace(/\s+#.*$/, '').trim();
    if (!line) continue;
    const kv = line.match(/^(repo|ref|readme)\s*:\s*(.+)$/i);
    if (!kv) spec.repo ??= line;
    else if (kv[1].toLowerCase() === 'readme') spec.readme = kv[2].trim() !== 'false';
    else spec[kv[1].toLowerCase()] = kv[2].trim();
  }
  const m = spec.repo?.match(/^(?:https?:\/\/github\.com\/)?([\w.-]+)\/([\w.-]+?)(?:\.git)?\/?$/);
  if (!m) return null;
  return { ...spec, owner: m[1], name: m[2], key: `${m[1]}/${m[2]}@${spec.ref ?? ''}`.toLowerCase() };
}

async function github(url, accept) {
  const headers = { Accept: accept, 'User-Agent': 'knowledges-site' };
  if (process.env.GITHUB_TOKEN) headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
  const res = await fetch(url, { headers, signal: AbortSignal.timeout(10000) });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return accept.endsWith('raw') ? res.text() : res.json();
}

// Clone local (sous-module ou dépôt imbriqué) dont le remote origin désigne owner/name.
function localClone(owner, name) {
  const want = `/${owner}/${name}`.toLowerCase();
  const dirs = (dir) => {
    try {
      return readdirSync(dir, { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => path.join(dir, e.name));
    } catch {
      return [];
    }
  };
  for (const dir of dirs(COMPANIONS).flatMap(dirs)) {
    try {
      const url = execFileSync('git', ['-C', dir, 'remote', 'get-url', 'origin'], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
      if (url.trim().toLowerCase().replace(/\.git$/, '').endsWith(want)) return dir;
    } catch {}
  }
  return null;
}

async function fetchRepo(spec) {
  const { owner, name } = spec;
  const data = { info: null, readme: null, ref: spec.ref };
  try {
    data.info = await github(`https://api.github.com/repos/${owner}/${name}`, 'application/vnd.github+json');
    if (!data.info) throw new Error('dépôt introuvable ou privé');
    data.ref ??= data.info.default_branch;
    data.readme = await github(`https://api.github.com/repos/${owner}/${name}/readme?ref=${encodeURIComponent(data.ref)}`, 'application/vnd.github.raw');
  } catch (err) {
    const clone = localClone(owner, name);
    const readme = clone && ['README.md', 'readme.md', 'Readme.md'].map((f) => path.join(clone, f)).find((f) => existsSync(f));
    if (readme) data.readme = readFileSync(readme, 'utf8');
    data.ref ??= 'main';
    console.warn(`  ⚠ GitHub ${owner}/${name} : ${err.message} → ${clone ? 'clone local' : 'fiche réduite'}`);
  }
  repos.set(spec.key, data);
}

async function loadRepos(items) {
  const specs = new Map();
  for (const it of items) {
    for (const m of it.body.matchAll(GITHUB_FENCE)) {
      const spec = parseGithubBlock(m[2]);
      if (spec) specs.set(spec.key, spec);
      else console.warn(`  ⚠ bloc github illisible dans ${it.name}`);
    }
  }
  await Promise.all([...specs.values()].map(fetchRepo));
}

// Liens relatifs du README → page GitHub (liens) ou fichier brut (images).
function rewriteReadme(text, { owner, name, ref }) {
  const blob = `https://github.com/${owner}/${name}/blob/${ref}/`;
  const raw = `https://raw.githubusercontent.com/${owner}/${name}/${ref}/`;
  const relative = (u) => !/^([a-z][a-z0-9+.-]*:|#|\/\/)/i.test(u);
  const clean = (u) => u.replace(/^\.?\//, '');
  const title = new RegExp(`^#\\s+${name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\s*$`, 'i');
  return mapOutsideFences(text, (line) =>
    line
      .replace(title, '')
      .replace(/(!?)\[([^\]]*)\]\(([^)\s]+)([^)]*)\)/g, (all, bang, label, url, rest) =>
        relative(url) ? `${bang}[${label}](${(bang ? raw : blob) + clean(url)}${rest})` : all,
      )
      .replace(/(<img\b[^>]*\bsrc=["'])([^"']+)/gi, (all, pre, url) => (relative(url) ? pre + raw + clean(url) : all)),
  );
}

const GITHUB_ICON =
  '<svg viewBox="0 0 16 16" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>';

function renderRepoCard(spec) {
  const { owner, name } = spec;
  const data = repos.get(spec.key) ?? { info: null, readme: null, ref: spec.ref ?? 'main' };
  const repoUrl = `https://github.com/${owner}/${name}`;
  const info = data.info;
  const meta = [
    info?.description && escapeHtml(info.description),
    info?.language && escapeHtml(info.language),
    spec.ref && `<code>${escapeHtml(spec.ref)}</code>`,
    info?.pushed_at && `mis à jour le ${new Date(info.pushed_at).toLocaleDateString('fr-FR')}`,
  ].filter(Boolean);
  let readme = '';
  if (spec.readme) {
    readme = data.readme
      ? `<details class="readme" open><summary>README</summary>\n${md.render(rewriteReadme(data.readme, { owner, name, ref: data.ref }))}</details>`
      : '<p class="readme-missing">Pas de README.</p>';
  }
  const tree = spec.ref ? `/tree/${encodeURIComponent(spec.ref)}` : '';
  return `<div class="repo-card">
<div class="repo-head">${GITHUB_ICON}<span class="repo-name">${escapeHtml(owner)} / <strong>${escapeHtml(name)}</strong></span><a class="repo-link" href="${repoUrl}${tree}" target="_blank" rel="noopener">Voir sur GitHub ↗</a></div>
${meta.length ? `<p class="repo-meta">${meta.join(' · ')}</p>` : ''}
<div class="repo-clone"><code>git clone${spec.ref ? ` -b ${escapeHtml(spec.ref)}` : ''} ${repoUrl}.git</code><a href="${repoUrl}/archive/${encodeURIComponent(data.ref)}.zip">ZIP</a></div>
${readme}
</div>
`;
}

const defaultFence = md.renderer.rules.fence;
md.renderer.rules.fence = (tokens, idx, options, env, self) => {
  const spec = tokens[idx].info.trim() === 'github' && parseGithubBlock(tokens[idx].content);
  return spec ? renderRepoCard(spec) : defaultFence(tokens, idx, options, env, self);
};

// `?v=<empreinte du contenu>` : l'URL change dès que le fichier change, ce qui
// contourne le cache navigateur sans rien configurer côté nginx.
const hashes = new Map();
function versioned(url, file) {
  if (!hashes.has(file)) hashes.set(file, createHash('sha256').update(readFileSync(file)).digest('hex').slice(0, 10));
  return `${url}?v=${hashes.get(file)}`;
}

function pageShell(title, body, { crumbs = '' } = {}) {
  return `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escapeHtml(title)}</title>
<link rel="stylesheet" href="/assets/hljs.css">
<link rel="stylesheet" href="${versioned('/assets/site.css', path.join(HERE, 'assets/site.css'))}">
</head>
<body>
<header class="topbar"><a href="/">Games Programming</a>${crumbs}</header>
<main>
${body}
</main>
</body>
</html>
`;
}

// ---------------------------------------------------------------------------
// Page de séance : onglets Slides / Exercices / Ressources

// Active l'onglet désigné par le hash (#slides par défaut). Sans JS, tout reste visible.
const TABS_SCRIPT = `(() => {
  const tabs = [...document.querySelectorAll('.tabs [data-tab]')];
  const show = (name) => {
    const tab = tabs.find((t) => t.dataset.tab === name && !t.disabled) ?? tabs[0];
    for (const t of tabs) {
      const on = t === tab;
      t.setAttribute('aria-selected', on);
      document.getElementById('tab-' + t.dataset.tab).hidden = !on;
    }
  };
  for (const t of tabs) t.addEventListener('click', () => { history.replaceState(null, '', '#' + t.dataset.tab); show(t.dataset.tab); });
  addEventListener('hashchange', () => show(location.hash.slice(1)));
  show(location.hash.slice(1));
})();`;

async function renderSeance(seance, resolver) {
  const docs = (list) => list.map((it) => `<article>\n${md.render(resolver.markdown(it, it.body))}</article>`).join('\n');
  const panels = [
    {
      id: 'slides',
      label: 'Slides',
      count: null,
      html: `<iframe class="deck-frame" src="slides/" title="${escapeHtml(seance.title)}" allowfullscreen></iframe>
<p class="deck-actions"><a href="slides/" target="_blank" rel="noopener">Plein écran ↗</a></p>`,
    },
    { id: 'exercices', label: 'Exercices', count: seance.exercises.length, html: docs(seance.exercises) },
    { id: 'ressources', label: 'Ressources', count: seance.resources.length, html: docs(seance.resources) },
  ];

  const tabs = panels
    .map((p) => {
      const count = p.count === null ? '' : ` <small>${p.count}</small>`;
      return `<button type="button" role="tab" data-tab="${p.id}"${p.count === 0 ? ' disabled' : ''}>${p.label}${count}</button>`;
    })
    .join('');
  const sections = panels.map((p) => `<section class="tab-panel" id="tab-${p.id}" role="tabpanel">\n${p.html}\n</section>`).join('\n');

  const crumbs = ` <span>›</span> ${escapeHtml(seance.category)} <span>›</span> ${escapeHtml(seance.code)}`;
  const body = `<p class="code">${escapeHtml(seance.code)}</p>
<h1>${escapeHtml(seance.title)}</h1>
<nav class="tabs" role="tablist">${tabs}</nav>
${sections}
<script>${TABS_SCRIPT}</script>`;
  await writeFile(path.join(seance.out, 'index.html'), pageShell(`${seance.code} - ${seance.title}`, body, { crumbs }));
}

// ---------------------------------------------------------------------------
// Accueil

async function renderIndex(seances) {
  const categories = [...new Set(seances.map((s) => s.category))].sort((a, b) => a.localeCompare(b, 'fr'));
  const blocks = categories.map((cat) => {
    const lis = seances
      .filter((s) => s.category === cat)
      .map((s) => `<li><a href="${s.url}"><span class="code">${escapeHtml(s.code)}</span>${escapeHtml(s.title)}</a></li>`)
      .join('\n');
    return `<section class="category"><h2>${escapeHtml(cat)}</h2><ul class="seance-list">\n${lis}\n</ul></section>`;
  });
  const empty = seances.length ? '' : '<p class="lead">Aucune séance publiée pour le moment.</p>';
  const body = `<h1>Games Programming</h1>\n<p class="lead">SAE Institute Genève</p>\n${empty}${blocks.join('\n')}`;
  await writeFile(path.join(DIST, 'index.html'), pageShell('Games Programming', body));
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
  const seances = buildSeances(items);
  const published = items.filter((it) => it.url);
  const resolver = new Resolver(published, imageIndex);
  await loadRepos(published.filter((it) => it.kind.dir !== 'slides'));

  for (const seance of seances) {
    console.log(`${seance.category} / ${seance.code} - ${seance.title}`);
    for (const it of [...seance.exercises, ...seance.resources]) console.log(`  ${it.kind.label.padEnd(10)} ${it.name}`);
    await renderDeck(seance, resolver, themes);
    await renderSeance(seance, resolver);
  }
  await renderIndex(seances);
  await copyAssets(resolver);

  console.log(`\n${seances.length} séance(s) active(s), ${published.length} documents → ${path.relative(ROOT, DIST)}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
