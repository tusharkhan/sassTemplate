# tools/ — page generator

**Development tool. Delete this folder before packaging the distribution zip.**

The template ships as plain static HTML: no runtime includes, no server, no
build step beyond Tailwind. Every page therefore carries its own physical copy
of the header and footer — roughly 250 lines duplicated ten times over.

That is what a buyer expects to receive, but it is a poor thing to maintain by
hand: changing one nav link means editing ten files identically, and the tenth
one is where the typo lives. This generator assembles the pages from shared
partials so the duplicated markup cannot drift.

The output is still ordinary static HTML with everything inlined. Nothing here
runs in the browser, and nothing here is needed to use the template.

## Usage

Requires Python 3.8+ and no packages.

```bash
python3 tools/build.py                  # regenerate every page
python3 tools/build.py pricing.html     # regenerate one page
python3 tools/build.py --check          # verify pages match their sources
npm run build                           # recompile Tailwind afterwards
```

`--check` exits non-zero and prints `STALE` for any page whose file on disk
differs from what the sources would produce. It is the useful one to run before
committing, and it currently passes for all ten pages — including `index.html`,
which round-trips byte for byte.

Convenience wrappers exist in `package.json`:

```bash
npm run pages
npm run pages:check
```

## Layout

```
tools/
  build.py                assembly logic
  pages.py                page registry — titles, meta, nav state
  partials/
    head.html             <head>, with __TITLE__ / __DESC__ / __OGDESC__ slots
    header.html           <body> open + skip link + navbar
    footer.html           CTA banner + </main> + footer + back-to-top + scripts
    auth-header.html      minimal chrome for login / register / forgot-password
    auth-footer.html      legal bar + scripts
  content/
    <page>.html           the <main> content unique to each page
```

A page is `head + header + content + footer`. Two shells exist: `site` (the
full navbar and six-column footer) and `auth` (logo, theme toggle and a thin
legal bar — a centred sign-in card under the full footer reads wrong).

## Editing

**Change the nav, logo or footer** — edit the partial, run `python3
tools/build.py`, then `npm run build`. Never edit the header or footer inside a
generated page; the next build overwrites it.

**Change one page's content** — edit `content/<page>.html`, then rebuild. The
content files hold everything from `<main>` onwards, excluding the shared CTA
banner (`cta=False` in the registry drops that banner for pages such as
`contact.html`, which ends on its own FAQ instead).

**Change a title or meta description** — edit `pages.py`.

**Add a page** — write `content/<page>.html`, add a `register(...)` call to
`pages.py`, rebuild. Set `active=` to the nav href that should be highlighted;
the generator adds `aria-current="page"` and a stronger text colour to both the
desktop and mobile-drawer copies of that link.

## Conventions the pages follow

Worth preserving in anything new, since they are what keeps the template
passing review:

- Semantic sectioning (`header`, `nav`, `main`, `section`, `article`, `aside`,
  `footer`), each section labelled with `aria-labelledby`, exactly one `<h1>`
  per page.
- No inline `style` attributes and no `on*` event handlers — styling is Tailwind
  utilities or the component classes in `src/input.css`, and interactivity is
  the `data-*` contract in `assets/js/main.js` (`data-reveal`, `data-accordion`,
  `data-billing-toggle`, `data-copy`, `data-theme-toggle`).
- Decorative SVGs carry `aria-hidden="true"`; meaningful ones get
  `role="img"` and a label.
- Wide tables live inside `overflow-x-auto` with a `min-w-*` so they scroll
  rather than breaking the page on mobile.
- Realistic copy throughout — no Lorem Ipsum, per Envato's review guidelines.
- Placeholder artwork is inline SVG or a CSS gradient, never a downloaded
  image. Comments mark where a buyer should drop in CC0 photography.
