#!/usr/bin/env bash
#
# Build the marketplace distribution zip.
#
#   bash tools/package.sh [version]
#
# Produces dist/wavenode-html-template-<version>.zip laid out the way Envato
# expects: a single root folder containing the site files and the buyer
# documentation, with every development artefact excluded.
#
# Excluded deliberately: node_modules/, tools/ (this script, the generator and
# the build blueprint), .git/, and the working-tree dotfiles. src/, package.json
# and tailwind.config.js ARE included — buyers legitimately need them to
# recompile the stylesheet.

set -euo pipefail

VERSION="${1:-1.0.0}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="wavenode-html-template"
STAGE="$ROOT/dist/$NAME"
ZIP="$ROOT/dist/$NAME-$VERSION.zip"

cd "$ROOT"

# --- refuse to package a stale or unbuilt tree ---------------------------------
if command -v python3 >/dev/null 2>&1; then
  echo "→ checking generated pages are in sync"
  python3 tools/build.py --check >/dev/null || {
    echo "✗ pages are out of sync with tools/content — run: npm run pages" >&2
    exit 1
  }
fi

if [ ! -s assets/css/style.css ]; then
  echo "✗ assets/css/style.css missing or empty — run: npm run build" >&2
  exit 1
fi

if [ ! -f assets/fonts/OFL.txt ]; then
  echo "✗ assets/fonts/OFL.txt missing — the font licence must ship" >&2
  exit 1
fi

# --- stage ---------------------------------------------------------------------
echo "→ staging"
rm -rf "$ROOT/dist"
mkdir -p "$STAGE"

# Site files
cp ./*.html "$STAGE/"
cp robots.txt sitemap.xml "$STAGE/"
cp README.md LICENSE.md CHANGELOG.md "$STAGE/"

# Assets, including the font licence
mkdir -p "$STAGE/assets"
cp -R assets/css assets/js assets/fonts assets/images "$STAGE/assets/"

# Sources a buyer needs to recompile
mkdir -p "$STAGE/src"
cp src/input.css "$STAGE/src/"
cp package.json tailwind.config.js "$STAGE/"

# Buyer documentation
mkdir -p "$STAGE/documentation"
cp documentation/index.html "$STAGE/documentation/"

# --- verify nothing developer-only slipped in ---------------------------------
echo "→ verifying"
for forbidden in node_modules tools .git AI_Sass_Template.md package-lock.json; do
  if find "$STAGE" -name "$forbidden" -print -quit | grep -q .; then
    echo "✗ '$forbidden' found in the staged tree" >&2
    exit 1
  fi
done

PAGES=$(find "$STAGE" -maxdepth 1 -name '*.html' | wc -l)
echo "  $PAGES pages, $(du -sh "$STAGE" | cut -f1) staged"

# --- zip -----------------------------------------------------------------------
echo "→ zipping"
( cd "$ROOT/dist" && zip -rq "$(basename "$ZIP")" "$NAME" -x '*.DS_Store' )
rm -rf "$STAGE"

echo "✓ $ZIP ($(du -h "$ZIP" | cut -f1))"
