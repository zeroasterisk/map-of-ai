# Samples rendered biome-fill colours: 300 isPointInFill hits per continent → mean RGB / HSL / HSV saturation / chroma.
# Usage (needs the headless-chromium-sandbox env vars): uv run --with playwright --with pillow python scripts/sample_fill_colours.py <url> <out.png>
# Use this to verify any colour change on the map — reading the hex in index.html is NOT evidence (v10 lesson).
import asyncio, sys, colorsys, io
from playwright.async_api import async_playwright
from PIL import Image
url, out = sys.argv[1], sys.argv[2]
JS = '''() => { const svg=document.querySelector('svg'); const res={};
 [...document.querySelectorAll('.continent')].forEach(g=>{const p=g.querySelector('path.land'); const r=p.getBoundingClientRect(); const pts=[];
  const ctm=p.getScreenCTM().inverse();
  for(let i=0;i<2500 && pts.length<300;i++){ const sx=r.x+Math.random()*r.width, sy=r.y+Math.random()*r.height;
   const pt=new DOMPoint(sx,sy).matrixTransform(ctm); if(p.isPointInFill(pt)) pts.push([sx,sy]); }
  res[g.dataset.id]=pts;}); return res; }'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width':1900,'height':1100}, device_scale_factor=2)
        await pg.goto(url, wait_until='networkidle', timeout=30000); await pg.wait_for_timeout(2000)
        await pg.screenshot(path=out, full_page=True)
        pts = await pg.evaluate(JS); await b.close()
    im = Image.open(out).convert('RGB'); W,H = im.size
    print(f"{'id':26s} {'meanRGB':16s} HSLsat HSVsat chroma")
    for k,v in pts.items():
        acc=[0,0,0]; n=0; sats=[]
        for sx,sy in v:
            x,y=int(sx*2),int(sy*2)
            if 0<=x<W and 0<=y<H:
                r,g,b_=im.getpixel((x,y)); acc[0]+=r;acc[1]+=g;acc[2]+=b_; n+=1
        if not n: continue
        m=[a/n for a in acc]; h,l,s=colorsys.rgb_to_hls(*[c/255 for c in m]); hv,sv,vv=colorsys.rgb_to_hsv(*[c/255 for c in m])
        print(f"{k:26s} {str(tuple(int(c) for c in m)):16s} {s:.3f}  {sv:.3f}  {max(m)-min(m):.0f}  n={n}")
asyncio.run(main())
