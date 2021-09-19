#!/usr/bin/env python3

import requests
import random

indices = list(range(1, 227))
random.shuffle(indices)
for i in indices:
    r = requests.get("https://www.cvk.gov.ua/pls/vp2019/wp336pt001f01=720pt005f01=%d.html" % i)
    with open("webArchive/%d.html" % i, "wb") as f:
        f.write(r.content.decode('cp1251').encode('utf8'))
        print(i)
