#!/usr/bin/env python3
"""
WaveNode — static page generator (development tool, not part of the template).

The template ships as plain, self-contained HTML files: no runtime includes,
no server, no build step beyond Tailwind. That means the header and footer
markup is physically duplicated into every page — which is what a buyer
expects, but it also means a nav change is a 23-file edit that quietly
drifts out of sync.

This script removes that risk. Each page is assembled from:

    partials/head.html      <head> block, with title/description slots
    partials/header.html    <body> open + skip link + navbar (site pages)
    partials/footer.html    CTA banner + </main> + footer + scripts
    partials/auth-header.html   minimal chrome for login/register
    partials/auth-footer.html   legal bar + scripts
    content/<page>.html     the <main> content unique to that page

The output is still ordinary static HTML with everything inlined — the
generator is a convenience for whoever maintains the template, and can be
deleted from the distribution zip.

Usage
-----
    python3 tools/build.py                     # regenerate every page
    python3 tools/build.py pricing.html        # regenerate one page
    python3 tools/build.py --check             # verify files match sources

After editing markup, rebuild the stylesheet so any new utility classes are
compiled:

    npm run build

Adding a page
-------------
1. Write the <main> content to content/<page>.html
2. Add a register(...) call to pages.py
3. Run this script, then `npm run build`
"""

import pathlib
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
ROOT = TOOLS.parent
PARTIALS = TOOLS / 'partials'
CONTENT = TOOLS / 'content'

# Public base URL, used for <link rel="canonical"> and og:url.
# Buyers: set this to your own domain (no trailing slash) and rebuild.
SITE_URL = 'https://wavenode.io'

# Absolute URL of the social-share image (1200x630).
OG_IMAGE = SITE_URL + '/assets/images/og-preview.png'

# Classes added to the nav link matching the current page.
ACTIVE_CLASSES = ' !text-slate-900 dark:!text-white'

# The two nav-link variants in header.html: desktop bar and mobile drawer.
NAV_LINK_CLASSES = ('class="nav-link"', 'class="nav-link py-3 text-base"')


def read(path):
    return path.read_text(encoding='utf-8')


PARTS = {name: read(PARTIALS / (name + '.html'))
         for name in ('head', 'header', 'footer', 'auth-header', 'auth-footer')}


# ---------------------------------------------------------------------------
# Page registry — populated by pages.py
# ---------------------------------------------------------------------------

PAGES = {}


def register(filename, title, description, og_description,
             active=None, cta=True, shell='site'):
    """Declare a page.

    filename        output file, written to the repository root
    title           <title> and og:title
    description     meta description
    og_description  shorter og:description
    active          nav href to mark as the current page (e.g. 'pricing.html')
    cta             include the shared CTA banner above the footer
    shell           'site' for the full navbar/footer, 'auth' for the
                    minimal login/register chrome
    """
    PAGES[filename] = {
        'title': title,
        'description': description,
        'og_description': og_description,
        'active': active,
        'cta': cta,
        'shell': shell,
    }


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def build_head(page, filename):
    # index.html canonicalises to the bare directory URL.
    slug = '' if filename == 'index.html' else filename
    return (PARTS['head']
            .replace('__TITLE__', page['title'])
            .replace('__DESC__', page['description'])
            .replace('__OGDESC__', page['og_description'])
            .replace('__CANONICAL__', SITE_URL + '/' + slug)
            .replace('__OGIMAGE__', OG_IMAGE))


def mark_active(header, active):
    """Give the current page's nav link aria-current and a stronger colour."""
    if not active:
        return header
    for classes in NAV_LINK_CLASSES:
        old = '<a href="%s" %s>' % (active, classes)
        new = '<a href="%s" %s aria-current="page">' % (
            active, classes[:-1] + ACTIVE_CLASSES + '"')
        header = header.replace(old, new)
    return header


def strip_cta(footer):
    """Drop the shared CTA banner, keeping </main> and everything after it."""
    start = footer.index('    <!-- ====')
    end = footer.index('  </main>')
    return footer[:start] + footer[end:]


def render(filename):
    page = PAGES[filename]
    content = read(CONTENT / filename)

    if page['shell'] == 'auth':
        return (build_head(page, filename)
                + PARTS['auth-header'] + '\n'
                + content + '\n'
                + PARTS['auth-footer'])

    footer = PARTS['footer'] if page['cta'] else strip_cta(PARTS['footer'])
    return (build_head(page, filename)
            + mark_active(PARTS['header'], page['active']) + '\n'
            + content + '\n'
            + footer)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv):
    check_only = '--check' in argv
    targets = [a for a in argv if not a.startswith('-')] or sorted(PAGES)

    unknown = [t for t in targets if t not in PAGES]
    if unknown:
        sys.stderr.write('unknown page(s): %s\n' % ', '.join(unknown))
        sys.stderr.write('known pages: %s\n' % ', '.join(sorted(PAGES)))
        return 2

    stale = []
    for filename in targets:
        output = render(filename)
        destination = ROOT / filename

        if check_only:
            current = read(destination) if destination.exists() else None
            if current != output:
                stale.append(filename)
                print('STALE  %s' % filename)
            else:
                print('ok     %s' % filename)
            continue

        destination.write_text(output, encoding='utf-8')
        print('wrote  %-22s %6d bytes' % (filename, len(output)))

    if check_only and stale:
        sys.stderr.write(
            '\n%d file(s) differ from their sources. '
            'Run `python3 tools/build.py` to regenerate.\n' % len(stale))
        return 1

    if not check_only:
        print('\nRemember to run `npm run build` if you added utility classes.')
    return 0


if __name__ == '__main__':
    exec(read(TOOLS / 'pages.py'))
    sys.exit(main(sys.argv[1:]))
