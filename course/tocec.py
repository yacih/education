
import requests
from bs4 import BeautifulSoup
url='https://www.tocec.org.tw/web/school_results.jsp'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

def page(id):
    url='https://www.tocec.org.tw/web/school_results.jsp?s_group_id='+id
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')
    page=sp.find('span',{'class':'text-info'})
    p=int(page.text)
    if p%10==1 or p%10==0:
        p=int(p/10)
    else:
        p=int(p/10+1)
    for j in range(1, p+1):
        coursename(id,str(j))

def coursename(id,p):
        url='https://www.tocec.org.tw/web/school_results.jsp?s_group_id='+id
        payload = 'page_num='+p
        print(payload)
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID=E07450B9DA577F553F651C344BD958DE'}
        html = requests.request("POST", url, headers=headers, data = payload)
        sp = BeautifulSoup(html.text, 'html.parser')####
        nam=sp.select('tbody a')
        for a in nam:
                print(a.text.strip())
                link=str('https://www.tocec.org.tw/web/'+a.get('href'))
                print(link) 

option=sp.select('#s_group_id option')
option.remove(option[0])
course={}
for o in option:
    c=dict([((o.text).replace('\n',""),o.get('value'))])
    course.update(c)
for c in course.values():
    print(c)
    page(c)


#----------

'''
import requests
import urllib.request as req
import urllib
import string
import bs4 as bs # BeautifulSoup

bookload = {
"page_num": '2',
"s_group_id": '15',
"s_field_id": "",
"s_school_id": "",
"s_search_tag":"" ,
"s_search_item": 0 
}
headers = {
"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
sourceCode = requests.post("https://www.tocec.org.tw/web/school_results.jsp",data=bookload,headers=headers)
html = bs.BeautifulSoup(sourceCode.text, 'html.parser')
# html

course_list=html.select(".table.table-hover.mb-4 tr")
course_title=[title.text for title in course_list[0].select("th")]
course_list.remove(course_list[0])
course=[name.text for course in course_list for name in course.select("td")]
course
#course_title
'''
