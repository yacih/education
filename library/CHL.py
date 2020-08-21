#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 08:35:41 2020

@author: yaci
"""

import requests
from bs4 import BeautifulSoup
x=input("請輸入書名:")
url = 'https://library.toread.bocach.gov.tw/toread/opac/search?q='+x+'&view=CONTENT'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

str1=sp.find_all('li',{'class':'reslt_item_head'},limit=10)
str2=sp.find_all('span',{'class':'crs_author'})
#str3=sp.find_all('div',{'class':'displayElementText ISBN'})
#str3=min(len(str1),len(str2))
print(str2.text)

#for i in str3:
#    print("書名："+str1[i].text+"作者"+str2[i].text)

dic=sp.find_all('div',{'class':'clear srch_reslt_list'})#抓表格
form=list()#[1,2,3,4]
bn=list()#書名
by=list()#作者
isbn=list()
for d in dic:#個別儲存表格進list-->儲存表格
    form.append(d)
for f in form:
    bn=f.find_all('li',{'class':'reslt_item_head'},limit=10)
    by=f.find_all('span',{'class':'crs_author'},limit=10)
    isbn=f.find_all('span',{'class':'crs_isbn'},limit=10)


    print(bn.text.strip())
    print(by.text.strip())   
    print(isbn.text.strip())   