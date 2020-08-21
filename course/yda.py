# -*- coding: utf-8 -*-
#p1
'''
import requests
from bs4 import BeautifulSoup
url = 'https://www.yda.gov.tw/index.aspx?SiteID=563426067575657313'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
title=sp.select('.tab_title')
cont=sp.select('.tab_cont')
art=[]
arc=[]
for c in title:
    art.append(c)
for c in cont:
    arc.append(c)

print(art[1].text)
print(arc[1].text)
print(art[3].text)
print(arc[3].text)
print(art[5].text)
print(arc[5].text)
'''
#p2
import requests
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('workilfe.db')
conn.execute("DELETE TABLE WK_PUBLIC")
conn.execute("DELETE TABLE WK_CAREER")
conn.execute("DELETE TABLE WK_TALENT")
def ct(a,num):
  url = 'https://www.yda.gov.tw/content/ViewPage/List_news.aspx?&SiteID=563426067575657313&MmmID=564072527341460121&CatID=0&Cat1='+str(a)+'&SSize=20'
  html = requests.get(url)
  sp = BeautifulSoup(html.text, 'html.parser')
  date=sp.select('.ListTable .date')
  context=sp.select('.ListTable a')
  dt=[i.text.strip() for i in date]
  tt=[i.text.strip() for i in context]
  ct=[i.get('href') for i in context]  
  for i in range(0,len(ct)):
    l=i+1
    #print(dt[l])#發布日期
    #print(tt[i])#公告名稱
    st=(ct[i])
    link='https://www.yda.gov.tw/content'+st[2:len(ct[i])]
    #print('https://www.yda.gov.tw/content'+st[2:len(ct[i])])#網址
    if num==1:
        cag='WK_CAREER'
        sql_str = "insert into WK_CAREER(WK_ID,NAME,DATE,WEB) values('{}','{}','{}','{}');".format(cag,tt[i],dt[l],link)
        conn.execute(sql_str)
        conn.commit()
    if num==2:
        cag='WK_PUBLIC'
        sql_str = "insert into WK_PUBLIC(WK_ID,NAME,DATE,WEB) values('{}','{}','{}','{}');".format(cag,tt[i],dt[l],link)
        conn.execute(sql_str)
        conn.commit()
    if num==3:
        cag='WK_TALENT'
        sql_str = "insert into WK_TALENT(WK_ID,NAME,DATE,WEB) values('{}','{}','{}','{}');".format(cag,tt[i],dt[l],link)
        conn.execute(sql_str)
        conn.commit()
i=1   # 索引變數
while i<5:
    if i==1:
        print('徵求人才:')
        ct(563426103271036540,i)
    elif i==2:
        print('生涯輔導:')
        ct(563620306322227722,i)
    elif i==3:
        print('國際及體驗學習:')
        ct(563620323705737247,i)
    else:
        conn.close()
        print('close')
    i+=1



# print('徵求人才')
# ct(563426103271036540)
# #name1,age1 = profile()
# print('生涯輔導')
# ct(563620306322227722)
# print('國際及體驗學習')
# ct(563620323705737247)

'''
INSERT INTO 資料表名稱 (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (1, 'Paul', 32, 'California', 20000.00 );
'''