#!/usr/bin/env python3

# HOW TO USE:
# sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config tesseract-ocr-rus
# pip3 install pyppeteer tesserocr asyncio

import asyncio
from pyppeteer import launch
import tesserocr

img = "example.png"

async def download():
    browser = await launch({
        "headless": True,
        "defaultViewport": {
            "width":1920,
            "height":10800
      }})
    page = await browser.newPage()
    await page.goto('http://www.primorsk.vybory.izbirkom.ru/region/izbirkom?action=show&root=252000008&tvd=4254005265098&vrn=100100067795849&prver=0&pronetvd=null&region=25&sub_region=25&type=242&report_mode=null&fbclid=IwAR2gF-3jFgW-j6QOLKuRbVDHisiqGVISroTPjtP2Sm7bh0STXMT2BUR-nIU')
    await page.screenshot({'path': img, 'fullPage': 'true'})
    await browser.close()

def ocr():
    # print(tesserocr.get_languages())
    with tesserocr.PyTessBaseAPI(psm=tesserocr.PSM.AUTO_OSD) as api:
        api.SetImageFile(img)
        print(api.GetUTF8Text())

asyncio.get_event_loop().run_until_complete(download())
ocr()

