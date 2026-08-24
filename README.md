# WaveNode — AI SaaS HTML Template

A 24-page HTML template for an AI-powered video and audio streaming platform.
Tailwind CSS and dependency-free vanilla JavaScript. Dark and light themes.
No framework, no server, no build step required to use it.

**Full documentation: open [`documentation/index.html`](documentation/index.html)
in a browser.** It covers installation, rebranding, the JavaScript reference and
a pre-launch checklist. This file is the two-minute version.

---

## Quick start

Unzip and double-click `index.html`. That is the whole installation — it runs
offline, straight from the filesystem.

To deploy, upload the `.html` files plus `assets/`, `robots.txt` and
`sitemap.xml` to your web root. Leave `src/`, `documentation/`, `node_modules/`
and the config files behind; they are for development only.

## Recompiling the CSS

The stylesheet ships compiled and minified, so this is only needed if you add
new Tailwind utility classes or edit `tailwind.config.js`.

```bash
npm install       # one dev dependency: Tailwind CSS
npm run build     # rebuild assets/css/style.css, minified
npm run dev       # or watch while you work
```

Edit `src/input.css`, never `assets/css/style.css` — the latter is generated.

## What's inside

| | |
| --- | --- |
| **Pages** | 24 — 3 landing variants, features + feature detail, pricing, integrations, changelog, API docs, blog + article, about, careers, customers, help center, FAQ, terms, privacy, contact, 3 auth screens, dashboard, 404 |
| **CSS** | Tailwind CSS 3.4, compiled to a single 56 KB minified file |
| **JavaScript** | ~399 lines, no dependencies, all driven by `data-*` attributes |
| **Fonts** | Plus Jakarta Sans + JetBrains Mono, self-hosted variable woff2 |
| **Icons** | Original inline SVG — no icon library. The only bitmap in the template is the social share card |
| **Themes** | Dark and light, dark by default, remembered per visitor |

## Standards

- Every page passes the W3C Nu validator with zero errors.
- Semantic landmarks, one `<h1>` per page, labelled form controls, visible
  focus rings, `prefers-reduced-motion` support, WCAG AA text contrast in both
  themes.
- Unique titles and meta descriptions, canonical URLs, Open Graph and Twitter
  cards with a 1200×630 share image.
- No external requests of any kind — no CDN, no Google Fonts, no analytics.
  The template is fully self-contained and works offline.

## Before you launch

The demo content is realistic but entirely fictional. At minimum: wire up the
forms (all use `action="#"`), replace `terms.html` and `privacy.html` with real
legal text, remove the visible template notices, and replace the `wavenode.io`
domain in each page's canonical and Open Graph tags.

Section 8 of the documentation is a complete checklist.

## Licence

See [`LICENSE.md`](LICENSE.md). The bundled fonts are SIL OFL 1.1 — keep
`assets/fonts/OFL.txt` with them.

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md).
