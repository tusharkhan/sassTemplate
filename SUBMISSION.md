# Submission guide — WaveNode HTML Template

**Seller-only document. Do not include this file in the distribution zip.**
The zip is built from an explicit list in step 2, so it is excluded automatically.

Everything in the template itself is finished. What remains is packaging,
hosting a demo, and the listing copy.

---

## Before you start: verify current Envato requirements

Envato changes its preview-image dimensions, category structure and AI-content
policy periodically. **Read the requirements on the upload form itself** rather
than trusting the numbers in any guide, including this one. The two worth
checking specifically:

- Preview image and thumbnail pixel sizes (step 5).
- The current AI-content policy, and whether it requires disclosure for code
  items. If disclosure is required, disclose it — being found to have concealed
  it risks the item *and* the account, which is worse than declaring it.

---

## 1. Pre-flight checks

Run these from the project root. All should be clean before you package.

```bash
# Every internal link resolves
for f in *.html; do
  grep -o 'href="[a-zA-Z0-9_.-]*\.html[^"]*"' "$f" \
    | sed 's/href="//;s/"$//;s/#.*//' | sort -u | while read t; do
      [ -n "$t" ] && [ ! -f "$t" ] && echo "DEAD: $f -> $t"
    done
done

# The compiled stylesheet exists and the font licence is present
test -s assets/css/style.css && echo "css ok"
test -f assets/fonts/OFL.txt && echo "font licence ok"

# No external requests anywhere (should return nothing)
grep -oE '(src|href)="https?://[^"]*\.(css|js)"' *.html
```

### Manual checks that matter

- **Cross-browser.** Open `index.html` in Chrome, Safari and Edge, not just
  Firefox. This is on Envato's own checklist and is the easiest thing to fail on.
- **Both themes.** Click the theme toggle in the header on a few pages. Light
  mode is the less-travelled path.
- **Mobile.** Resize to ~390px wide. Check the wide tables on `features.html`
  and the code blocks on `docs.html` scroll inside their containers rather than
  breaking the page.
- **W3C.** Upload a few pages to https://validator.w3.org/nu/ — paste-by-file.
  Expect zero errors. Reports of `Attribute "media" not allowed on element
  "meta"` from older offline validators are a stale-spec artefact; the hosted
  validator accepts per-theme `theme-color`.

---

## 2. Build the distribution zip

There is no packaging script in the repo. Copy-paste this block; it stages an
explicit file list so nothing developer-only can leak in.

```bash
cd /path/to/sassTemplate
VERSION=1.0.0
NAME=wavenode-html-template
rm -rf /tmp/wnpack && D=/tmp/wnpack/$NAME && mkdir -p "$D"

# Site files
cp *.html robots.txt sitemap.xml "$D/"
cp README.md LICENSE.md CHANGELOG.md "$D/"

# Assets (includes assets/fonts/OFL.txt — the licence must ship with the fonts)
mkdir -p "$D/assets" && cp -R assets/css assets/js assets/fonts assets/images "$D/assets/"

# Sources a buyer needs to recompile the CSS
mkdir -p "$D/src" && cp src/input.css "$D/src/"
cp package.json tailwind.config.js "$D/"

# Buyer documentation
mkdir -p "$D/documentation" && cp documentation/index.html "$D/documentation/"

# Verify nothing developer-only slipped in
for x in node_modules package-lock.json .git dist SUBMISSION.md; do
  find "$D" -name "$x" -print -quit | grep -q . && echo "LEAKED: $x"
done

( cd /tmp/wnpack && zip -rq "$NAME-$VERSION.zip" "$NAME" -x '*.DS_Store' )
mv "/tmp/wnpack/$NAME-$VERSION.zip" . && rm -rf /tmp/wnpack
echo "built: $NAME-$VERSION.zip"
```

Expected result: roughly 444 KB, 24 `.html` files, a single root folder named
`wavenode-html-template`.

**Deliberately excluded:** `node_modules/`, `package-lock.json`, `.git/`,
`SUBMISSION.md`. **Deliberately included:** `src/input.css`, `package.json` and
`tailwind.config.js`, because buyers legitimately need them to recompile.

---

## 3. Host the live demo

ThemeForest will not accept a site template without a working live preview. The
template is pure static files, so this takes minutes.

| Option | How |
| --- | --- |
| Netlify Drop | Drag the project folder onto https://app.netlify.com/drop |
| GitHub Pages | Repo Settings → Pages → deploy from `main`, root |
| Cloudflare Pages | Connect the repo, no build command, output dir `/` |
| Your own server | Upload `*.html`, `assets/`, `robots.txt`, `sitemap.xml` |

Only those four items are needed on the web server. `src/`, `documentation/`,
`node_modules/` and the config files are not.

Configure the 404 page so it is actually served:

- **Apache** — add `ErrorDocument 404 /404.html` to `.htaccess`
- **Nginx** — add `error_page 404 /404.html;`
- **Netlify** — it uses `404.html` automatically

---

## 4. Point the template at the demo domain

The canonical and Open Graph tags currently reference `wavenode.io`. Once the
demo URL is live:

```bash
# replace with your real demo host
find . -maxdepth 1 -name '*.html' -exec \
  sed -i 's|https://wavenode.io|https://your-demo-url.example|g' {} +
grep -c 'wavenode.io' *.html   # should be 0 for the URL (product names remain)
```

Then update the `Sitemap:` line in `robots.txt` and the `<loc>` entries in
`sitemap.xml`, and **rebuild the zip** (step 2).

---

## 5. Preview images

These are uploaded separately from the main zip; they are not inside it.

You need a thumbnail and a larger preview image. **Get the exact dimensions from
the upload form** — they have changed over the years and I am not going to
guess numbers you would then have to redo.

Notes:

- `assets/images/og-preview.png` is a social-share card (1200×630). It is not an
  Envato preview image, though it is a reasonable starting point for the design.
- Screenshots of `index.html`, `index-creator.html`, `pricing.html` and
  `user-dashboard.html` in dark mode show the template off best.
- If the preview images are **not** included in the buyer's download, say so in
  the item description. Envato asks for this explicitly.

---

## 6. Listing details

**Category:** Site Templates → Technology (Admin & Corporate is the alternative).

**Points worth putting in the description**, all of them verified rather than
aspirational:

- 24 pages, including three landing-page variants, an API documentation layout,
  a signed-in dashboard, three auth screens and a 404.
- Zero W3C validation errors on every page.
- No external requests at all — no CDN, no Google Fonts, no analytics. Works
  offline, straight from the filesystem.
- Tailwind CSS 3.4, compiled and minified; no build step required to use it.
- Dependency-free vanilla JavaScript, ~400 lines, driven by `data-*` attributes.
- Dark and light themes, remembered per visitor.
- Self-hosted variable fonts with the SIL OFL licence included.
- All icons and illustrations are original inline SVG — no icon library, no
  bitmap images, nothing to license.
- Accessibility: semantic landmarks, one `<h1>` per page, labelled form
  controls, visible focus rings, `prefers-reduced-motion` support, WCAG AA text
  contrast in both themes.
- A 10-section offline help file with a launch checklist.

**Browser support to state:** Chrome, Edge, Firefox, Safari — current versions.

---

## 7. Upload

Author dashboard → Upload Item:

1. Main file → the zip from step 2
2. Preview images → the bundle from step 5
3. Live demo URL → from step 3
4. Category, tags, description → step 6
5. Submit for review

Review typically takes a few days.

---

## 8. If it comes back rejected

Envato's feedback is usually specific. The most common causes for this kind of
item, and where each is already handled:

| Reason | Status |
| --- | --- |
| No documentation | `documentation/index.html`, 10 sections |
| Missing asset licences | `assets/fonts/OFL.txt` |
| W3C errors | Zero across all 24 pages |
| Broken links | Zero |
| Messy zip | Built from an allowlist in step 2 |
| Lorem Ipsum | None — all copy is original |
| Inline CSS or `on*` handlers | None |
| No live preview | Step 3 |

If the feedback is about **design** rather than compliance, that is a soft
rejection on aesthetics and needs design work, not fixes to the code.

---

## Reference: what is in the repo and why

| Path | Ships to buyer? | On web server? |
| --- | --- | --- |
| `*.html` (24) | yes | yes |
| `assets/` | yes | yes |
| `robots.txt`, `sitemap.xml` | yes | yes |
| `documentation/` | yes | no |
| `README.md`, `LICENSE.md`, `CHANGELOG.md` | yes | no |
| `src/input.css` | yes | no |
| `package.json`, `tailwind.config.js` | yes | no |
| `package-lock.json` | no | no |
| `node_modules/` | no | no |
| `SUBMISSION.md` | no | no |

Rebuilding the CSS needs `npm install` first — `node_modules/` is not committed.
Only necessary if you edit `src/input.css` or `tailwind.config.js`; the compiled
`assets/css/style.css` in the repo is current.

**One caveat about maintenance:** the header and footer are duplicated in all 24
pages. Changing a nav link means editing 24 files identically. The generator
that used to keep them in sync was removed; it is recoverable from git history
at commit `25151f0` if that becomes painful.
