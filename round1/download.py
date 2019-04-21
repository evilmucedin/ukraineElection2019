#!/usr/bin/env python3

import requests

for i in range(1, 227):
    r = requests.get("https://www.cvk.gov.ua/pls/vp2019/wp336pt001f01=719pt005f01=%d.html" % i)
    with open("webArchive/%d.html" % i, "wb") as f:
        f.write(r.content.decode('cp1251').encode('utf8'))
        print(i)
