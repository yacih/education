import requests
from bs4 import BeautifulSoup

'''def classname(id)
url='hhttps://cell.moe.edu.tw/Guests/CourCg.aspx?cg=%s&subcg=%s'%id #&subcg=%s
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')####
'''
import re


def runall(cg,subcg):
    
    url='https://cell.moe.edu.tw/Guests/CourCg.aspx?cg='+cg+'&subcg='+subcg
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')####   
    
    name=sp.select('a.hp3')
    #ima=sp.find_all('div',{'a':'class herf'},{'img':'alt'})
    #nam=sp.find_all('div',{'class':'coursename'})
    #nam=sp.select('div .coursename h4')
    na=[na.text for na in name]
    #print(len(na))
    for list in na:
        print(list)     


def courseid(id):

    url='https://cell.moe.edu.tw/Guests/CourCg.aspx?cg=%s'%id
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')####

    coursess_text = sp.find_all('select')[2]
    coursesss=sp.select('#MainContent_ddlSubcg option')
    coursesss.remove(coursesss[0])

    ccname={}
            
    for o in coursesss:
        r=dict([((o.text).replace('\n',""),o.get('value'))])
        ccname.update(r)
        #print(o.text.strip())
            
    for s in ccname.values():
        print(s)
        (cg,subcg)=(cc,s)
        runall(cg,subcg)




url='https://cell.moe.edu.tw/Guests/CourCg.aspx?cg=163'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')####
courses_text = sp.find_all('select')[1]
course=sp.select('#MainContent_ddlCg option')
course.remove(course[0])
cname={}



for c in course:
    d=dict([((c.text).replace('\n',""),c.get('value'))])
    cname.update(d)
    print(c.text.strip())

for cc in cname.values(): 
    #id=cc
    print(cc)
    id=cc
    courseid(id)