#!/usr/bin/env node
// scripts/build_glyphs.js — generate MapLibre SDF glyph PBFs (site/v2/glyphs/<stack>/<start>-<end>.pbf)
// from OFL TTFs with fontnik. Usage:
//   node scripts/build_glyphs.js <fontdir>            (fontdir contains Cinzel[wght].ttf, Lora[wght].ttf, Lora-Italic[wght].ttf)
// Requires: npm install fontnik  (NODE_PATH pointing at its node_modules, e.g. /tmp/mlb/node_modules).
// Fonts: Cinzel (SIL OFL 1.1) and Lora (SIL OFL 1.1) from github.com/google/fonts — the same families atlas.html
// loads from Google Fonts. Variable fonts are instanced at their default axis position (Cinzel 400, Lora 400) by
// freetype inside fontnik; the "Cinzel SemiBold" stack is the same file (fontnik ignores named instances), kept as a
// separate stack name so style.json can switch to a real semibold cut later without touching layers.
// Only ranges 0–2303 (Basic Latin … Greek/Cyrillic) plus 8192–8447 (punctuation/dashes/arrows) are emitted; that
// covers every string in site/entities.json (verified by export_geojson.py, which warns on any codepoint outside).
const fs = require('fs'), path = require('path');
const fontnik = require('fontnik');
const fontdir = process.argv[2] || '/tmp/fonts';
const out = path.join(__dirname, '..', 'site', 'v2', 'glyphs');
const STACKS = {
  'Cinzel Regular': 'Cinzel[wght].ttf',
  'Lora Regular': 'Lora[wght].ttf',
  'Lora Italic': 'Lora-Italic[wght].ttf',
};
const RANGES = [];
for (let s = 0; s < 2304; s += 256) RANGES.push([s, s + 255]);
for (let s = 8192; s < 8448; s += 256) RANGES.push([s, s + 255]);
RANGES.push([9472, 9727]); // box drawing / misc technical (arrows like → are in 8592-8703 → covered by 8448-8703 below)
RANGES.push([8448, 8703]);
(async () => {
  for (const [stack, file] of Object.entries(STACKS)) {
    const buf = fs.readFileSync(path.join(fontdir, file));
    const dir = path.join(out, stack); fs.mkdirSync(dir, {recursive: true});
    let n = 0;
    for (const [start, end] of RANGES) {
      const pbf = await new Promise((res, rej) => fontnik.range({font: buf, start, end}, (e, d) => e ? rej(e) : res(d)));
      fs.writeFileSync(path.join(dir, `${start}-${end}.pbf`), pbf); n++;
    }
    console.log(`${stack}: ${n} ranges -> ${dir}`);
  }
})().catch(e => { console.error(e); process.exit(1); });
