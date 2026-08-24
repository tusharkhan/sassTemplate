# Changelog — WaveNode HTML Template

All notable changes to this template are recorded here.
This project follows [Semantic Versioning](https://semver.org).

## [1.0.0] — 2026-08-24

Initial release.

- 23 static HTML pages: 3 landing variants, features, pricing, integrations,
  changelog, API docs, blog index + article, about, careers, customers,
  help centre, FAQ, terms, privacy, contact, 3 auth screens, dashboard, 404.
- Tailwind CSS 3.4, compiled and minified — no build step required to use.
- Dependency-free vanilla JavaScript (~290 lines): theme toggle with
  persistence, sticky header, mobile drawer, scroll reveal, accordions,
  pricing toggle, copy-to-clipboard, back-to-top.
- Dark and light themes, dark by default, remembered per visitor.
- Two self-hosted variable fonts (Plus Jakarta Sans, JetBrains Mono) with
  the SIL OFL licence included. No CDN, no external requests.
- All artwork is original inline SVG or CSS gradient — no image licensing.
- Every page validates against the W3C Nu checker with zero errors and
  zero warnings.
- Accessibility: semantic landmarks, one `<h1>` per page, labelled forms,
  visible focus rings, `prefers-reduced-motion` support, keyboard-reachable
  scroll regions, WCAG AA text contrast in both themes.
- SEO: unique titles and meta descriptions, canonical URLs, Open Graph and
  Twitter cards with a 1200×630 share image, `robots.txt`, `sitemap.xml`.
- Optional Python page generator in `tools/` keeps the duplicated header and
  footer in sync across all 23 pages.
