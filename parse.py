
#!/usr/bin/env python3

# HOW TO USE:
# sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config tesseract-ocr-rus
# pip3 install pyppeteer tesserocr

import asyncio
from pyppeteer import launch
import tesserocr
import logging
import os

img = "page.png"
url = 'http://www.primorsk.vybory.izbirkom.ru/region/izbirkom?action=show&root=252000008&tvd=4254005265098&vrn=100100067795849&prver=0&pronetvd=null&region=25&sub_region=25&type=242&report_mode=null'

logging.basicConfig(level=os.getenv("LOGGING", logging.INFO))

async def main():
    logging.info("Launching browser...")
    browser = await launch({
        "args": ['--no-sandbox'],
        "headless": True,
        "defaultViewport": {
            "width":1920,
            "height":3000
      }})
    logging.info(f"Opening {url}...")
    page = await browser.newPage()
    page.setDefaultNavigationTimeout(120000)
    await page.goto(url, {"waitUntil": "networkidle0"})
    await page.evaluate('''()=>{
        const p = document.getElementById("election-results").parentElement;
        p.setAttribute(
                "style",
                `
                    position: fixed;
                    top: 0; left: 0;
                    z-index: 999;
                    width: 100%;
                    background: white;
                    height: 100%;
                    font-size: 2em;
                    font-weight: bold;
                    text-align: right;
                `
            )
        p.querySelectorAll(".table-striped tr").forEach(t=>{
                t.setAttribute('style', 'width:100%; display:inline-block')
        })
        document.querySelectorAll("br").forEach(b=>b.style.display='none')
    }''')
    logging.info("Taking a screenshot...")
    await page.screenshot({'path': img, 'fullPage': 'true'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

with tesserocr.PyTessBaseAPI(psm=tesserocr.PSM.AUTO_OSD, lang='rus') as api:
    logging.info("Running optical character recognition...")
    api.SetImageFile(img)
    txt = api.GetUTF8Text()
    print(txt)
    logging.info("Writing results to file")
    with open("results.txt", "w") as f:
        f.write(txt)
