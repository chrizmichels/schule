#!/bin/bash
# Einmalig: Schriften und Python-Pakete installieren
cd "$(dirname "$0")"
mkdir -p fonts out && (cd fonts && npm init -y >/dev/null && npm i @fontsource/atkinson-hyperlegible @fontsource/caveat @fontsource/courier-prime @fontsource/zilla-slab)
pip install playwright qrcode pillow pymupdf && playwright install chromium
