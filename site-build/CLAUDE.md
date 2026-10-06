# site-build — le générateur du site

`build.mjs` est le générateur entier — un seul fichier, et son commentaire d'en-tête est la
spec. Plain Node >= 24, aucun framework, aucune dépendance de build.

## Commandes

```bash
cd site-build && npm ci && npm run build
```

```bash
cd site-build && npm run preview
```

`npm run build` écrit `site-build/dist/` (gitignoré) **sans les brouillons** — c'est le build
de production, celui que lance la CI. `npm run preview` rebuild **avec** les brouillons puis
sert le résultat : c'est le serveur de test des révisions. `npm run build:draft` fait le build
brouillons seul, `npm run serve` sert `dist/` tel quel.

Deux configs dans `.claude/launch.json`, à préférer à un `serve` lancé à la main :
`preview_start {name: "knowledges-site-draft"}` (rebuild brouillons + serveur, pour les
révisions) et `preview_start {name: "knowledges-site"}` (sert `dist/` en l'état).

`GITHUB_TOKEN` est optionnel et ne sert qu'à relever la limite de débit des blocs `github`
récupérés au build.

## Le contrat de publication

Le champ `publish` du frontmatter du deck a **trois états**, et c'est le seul levier :

| `publish` | Effet |
|---|---|
| `false` ou absent | non publié : la séance n'existe pas sur le site |
| `draft` | brouillon : rendu **uniquement** par un build `--drafts`, avec bandeau « brouillon », badge et `noindex` |
| `online` | en ligne, visible des étudiants |

`true` reste accepté comme alias historique d'`online`. Toute autre valeur est refusée avec
un avertissement et traitée comme non publiée : une faute de frappe ne met rien en ligne.

L'inclusion des brouillons est **opt-in** (`--drafts` ou `KNOWLEDGES_DRAFTS=1`) : un
`npm run build` nu ne peut pas publier un brouillon, même oublié en l'état, et la CI ne passe
jamais le flag. C'est la garantie qu'une séance en révision ne part pas chez les étudiants.

Les autres règles quand on édite des notes :

- Rien d'autre que `publish` ne déclenche la publication — en particulier pas la note de
  séance dans `lectures/`.
- Un exercice ou une ressource s'attache à une séance par `seances: [CODE, …]` en
  frontmatter, ou par un nom de fichier commençant par le code de la séance.
- Tout dossier dont le nom commence par `_` est ignoré — **sauf** sous `00 widgets/`, qui est
  copié en entier vers `/widgets/`.
- Les decks référencent un widget par son chemin **vault**
  (`00 widgets/_widgets/x.html#anchor`), qui est ce qu'Obsidian sert ; le build le réécrit en
  `/widgets/…`. Écrire le chemin vault, jamais `/widgets/…`.

## Déploiement

`.github/workflows/deploy-knowledges.yml`, à chaque push sur `main` touchant les slides, les
exercices, les images, les widgets, le CSS des decks ou `site-build/`. Il lance `npm run build`
(sans `--drafts`) et rsync `dist/` en **mode miroir (`--delete`)** : tout ce qui a été posé
sur le VPS à la main est effacé.

Ne jamais ajouter `--drafts` ni `KNOWLEDGES_DRAFTS` au workflow : c'est ce qui sépare le
serveur de test du site des étudiants.
