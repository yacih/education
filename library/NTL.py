 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 08:06:54 2020

@author: yaci
"""

import requests
from bs4 import BeautifulSoup
x=input("請輸入書名:")
url = 'https://nccc.ent.sirsi.net/client/zh_TW/main/search/results?qu='+x+'&te=ILS'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
  
str1=sp.select('.displayDetailLink',limit=10)
str2=sp.select('.displayElementText.highlightMe.INITIAL_AUTHOR_SRCH',limit=10)
str3=sp.select('.ISBN_value',limit=10)
#str3=sp.find_all('div',{'class':'displayElementText ISBN'})
#str3=min(len(str1),len(str2))


#print(sp)
#print(str2)
for i in str1:
    print("書名："+i.text)
for i in str2:
    print("作者："+i.text)
for i in str3:
    print("ISBN："+i.text)  
