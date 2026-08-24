# CLAUDE.md

Notes for working on this repo. Development-only — not shipped to buyers.

## What this is

**WaveNode**, a commercial HTML template for sale on ThemeForest. The fictional
product is an AI-powered video/audio streaming API platform. 24 static pages.

Not an app. Every page is plain HTML a buyer can double-click and open from the
filesystem. That constraint drives most of the decisions below.

## Stack

- **Tailwind CSS 3.4**, compiled to `assets/css/style.css` (committed, minified).
  Source is `src/input.css`. Never edit the compiled file.
- **Vanilla JS**, `assets/js/main.js` (~400 lines, 11 modules, IIFE, ES5-style).
  No dependencies, no framework.
- **Self-hosted variable fonts** — 4 woff2 files, Plus Jakarta Sans + JetBrains
  Mono. One file per family per subset; `font-weight: 200 800` ranges cover every
  weight. Do not split these back into per-weight files: they were 16 files that
  were only 4 unique payloads, and browsers fetched the same bytes 5× per family.
- **Inline SVG** for every icon, logo and illustration. No icon library, no
  bitmap images anywhere except `assets/images/og-preview.png`.

`node_modules/` is not committed. Run `npm install` before `npm run build`, and
only if you edited `src/input.css` or `tailwind.config.js`.

## Hard constraints (Envato review rules)

Breaking any of these risks rejection:

- **Zero W3C errors.** Validate before committing markup changes.
- **No inline `style=""`** and **no `on*` handlers**. Styling is Tailwind
  utilities or the component classes in `src/input.css`; behaviour is the
  `data-*` contract below.
- **No Lorem Ipsum.** All copy is original and specific.
- **No external requests.** No CDN, no Google Fonts, no analytics. The only
  `https://` strings in the HTML are text inside fictional code samples.
- **`assets/fonts/OFL.txt` must ship with the fonts.** SIL OFL requires it.

## Header/footer are duplicated in all 24 files

There is no build step and no includes, so the ~250 lines of header and footer
exist physically in every page. **Changing a nav link means editing 24 files
identically.**

A Python generator (`tools/`) used to keep them in sync from shared partials. It
was removed at the owner's request. If hand-editing 24 files becomes painful, it
is recoverable from git history at commit `25151f0` — it had a `--check` mode
that detected drift, and `index.html` round-tripped byte for byte.

When editing shared markup by hand, verify afterwards that all 24 copies match.

## JavaScript contract

`main.js` modules are keyed on `data-*` attributes and each returns early if its
markup is absent, so any section can be deleted without errors.

| Attribute | Behaviour |
| --- | --- |
| `data-theme-toggle` | dark/light, persisted to `localStorage['wavenode-theme']`; `aria-pressed` is initialised from the applied theme |
| `data-header` | adds `.is-scrolled` past 24px |
| `data-menu-toggle` / `data-mobile-menu` | drawer; focuses its first item on open and contains Tab |
| `data-reveal` (+ `data-reveal-delay="1..3"`) | IntersectionObserver fade-up |
| `data-accordion` / `-trigger` / `-panel` / `-group` | accordion; `-group` allows one open at a time |
| `data-billing-toggle`, `data-price-monthly`, `data-price-annual` | pricing switch, **defaults to annual** |
| `data-copy` + `data-copy-target="#id"` | clipboard; announces via `[data-copy-status]` |
| `data-back-to-top` | appears past 600px |
| `data-toc` | scrollspy — sets `aria-current` on the in-view section's TOC link |
| `data-year` | current year (footer copyright) |

Two things to preserve, both of which were bugs:

- The billing toggle's **static markup must match `aria-checked="true"`** — the
  monthly spans carry `hidden`, the annual ones do not. Otherwise the price
  visibly flashes on load and lies with JS disabled.
- `data-copy` buttons capture their original label **once, outside the click
  handler**. Capturing inside meant a double-click stuck on "Copied!" forever.

## Canonical demo figures — keep these consistent

`index.html` once contradicted the detail pages on nine metrics. If you change a
number, change it everywhere. Current values:

| Figure | Value |
| --- | --- |
| Median / p95 latency | 47ms / 91ms |
| Edge locations | 210+ |
| Minutes delivered per month | 1.2B |
| Uptime SLA | 99.99% |
| Customers | 4,000+ |
| Caption languages | 42 (free tier: 5) |
| Plans, monthly | $0 / $29 / $249 |
| Plans, annual | $0 / $23 / $199 — must be ~20% off, the advertised claim |
| Plan minutes | 1,000 / 20,000 / Unlimited |
| Max resolution | 720p / 4K / 4K HDR |
| Creator platform fee | 3%, payouts in 38 currencies within two business days |
| Company | founded 2017, 84 people, Berlin / Singapore / Austin |

## Conventions

- **British English prose** — monetisation, summarise, diarisation, licence,
  programme, behaviour, anonymised. "Help Center" stays American as a page name.
- **One person, one job.** The fictional cast recurs across pages; three
  characters once held two jobs each, most awkwardly a WaveNode employee also
  appearing as a customer giving a testimonial. Avatar initials must match the
  name.
- **Semantic sectioning** with `aria-labelledby` on each section, exactly one
  `<h1>` and one `<main>` per page.
- **Decorative SVGs** get `aria-hidden="true"`; meaningful ones get `role="img"`
  plus a label. Product mockups are wrapped in `aria-hidden` — their fake chat
  and transcript text is not real content.
- **Wide tables and code blocks** live in `overflow-x-auto` with `tabindex="0"`,
  so they are keyboard-scrollable.
- Placeholder markers a buyer must delete are **visible on the page** — the amber
  legal notices on `terms.html` / `privacy.html`, and notes on `contact.html`,
  `help-center.html` and `about.html`.

## Gotchas

- **`media` on `<meta name="theme-color">` is valid.** Offline validators built
  before ~2021 report it as an error. The hosted validator accepts it; confirmed
  by validating a page that contains it. Do not "fix" this.
- **`visibility` is a discrete property.** `transition: visibility 0.3s` flips it
  at the halfway point. The accordion uses a delay on close only, with
  `transition: none` on the open state. See `.accordion-panel` in `src/input.css`.
- **`grid-template-rows: 0fr` hides nothing from assistive tech.** Collapsed
  accordion panels need `visibility: hidden` or their links stay in the tab order.
- **Theme deliberately ignores `prefers-color-scheme`.** Dark is the default
  regardless of OS setting, so the demo lands dark for everyone. Product
  decision, not a bug; documented in the help file.
- **Screenshotting with headless Firefox**: snap-confined Firefox cannot read
  `/var/www` and gets a private `/tmp`, so it hangs. Serve over
  `http://127.0.0.1` and write output under `$HOME`. `--screenshot` captures at
  `load`, so any reporting harness must write results synchronously, and a
  persistent profile caches CSS — disable it or a fixed rule looks broken.

## Files

| Path | Ships to buyer | On web server |
| --- | --- | --- |
| `*.html` (24), `assets/`, `robots.txt`, `sitemap.xml` | yes | yes |
| `documentation/index.html` | yes | no |
| `README.md`, `LICENSE.md`, `CHANGELOG.md` | yes | no |
| `src/input.css`, `package.json`, `tailwind.config.js` | yes | no |
| `CLAUDE.md`, `SUBMISSION.md`, `package-lock.json`, `node_modules/` | no | no |

`SUBMISSION.md` step 2 has the packaging command; it stages an explicit
allowlist, so new dev files are excluded by default rather than by a rule
someone has to remember.
