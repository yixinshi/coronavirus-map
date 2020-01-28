# Lint as: python3
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import urllib3
import requests
import re
import json

url = "https://3g.dxy.cn/newh5/view/pneumonia"
html = requests.get(url)
parsed_html = BeautifulSoup(html.content, "html.parser")
x = parsed_html.body.find('script', attrs={'id':'getAreaStat'}).text
regex = "try\s\{\swindow\.getAreaStat\s=\s(\[.*\])\}catch\(e\)\{\}"
m = re.search(regex, x)
if m:
    r, = m.groups(1)
    r = json.loads(r)
    for x in r:
        print(x["provinceName"])
        print(x)
        break
else:
    print("no found")
