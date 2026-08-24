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
`sitemap.xml` to your web root. Leave `tools/`, `src/`, `documentation/`,
`node_modules/` and the config files behind; they are for development only.

## Recompiling the CSS

The stylesheet ships compiled and minified, so this is only needed if you add
new Tailwind utility classes or edit `tailwind.config.js`.

```bash
npm install       # one dev dependency: Tailwind CSS
npm run build     # rebuild assets/css/style.css, minified
npm run dev       # or watch while you work
```

Edit `src/input.css`, never `assets/css/style.css` — the latter is generated.

## Optional page generator

The header and footer are physically duplicated into all 24 pages, which is
what lets the template work with no server. A small Python script (no packages
needed) keeps those copies in sync so a nav change is one edit, not 24:

```bash
npm run pages         # regenerate all pages from tools/partials + tools/content
npm run pages:check   # verify nothing has drifted out of sync
npm run build         # then recompile the CSS
```

Delete `tools/` if you would rather edit the HTML by hand. Nothing in the
shipped site depends on it. See [`tools/README.md`](tools/README.md).

## What's inside

| | |
| --- | --- |
| **Pages** | 24 — 3 landing variants, features + feature detail, pricing, integrations, changelog, API docs, blog + article, about, careers, customers, help centre, FAQ, terms, privacy, contact, 3 auth screens, dashboard, 404 |
| **CSS** | Tailwind CSS 3.4, compiled to a single 56 KB minified file |
| **JavaScript** | ~399 lines, no dependencies, all driven by `data-*` attributes |
| **Fonts** | Plus Jakarta Sans + JetBrains Mono, self-hosted variable woff2 |
| **Icons** | Original inline SVG — no icon library, no image files |
| **Themes** | Dark and light, dark by default, remembered per visitor |

## Standards

- Every page passes the W3C Nu validator with zero errors and zero warnings.
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
legal text, remove the visible template notices, and set your own domain in
`SITE_URL` (`tools/build.py`).

Section 9 of the documentation is a complete checklist.

## Licence

See [`LICENSE.md`](LICENSE.md). The bundled fonts are SIL OFL 1.1 — keep
`assets/fonts/OFL.txt` with them.

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md).
