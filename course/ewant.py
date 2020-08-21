import requests
from bs4 import BeautifulSoup
url='https://www.ewant.org/admin/tool/mooccourse/allcourses.php?method=0&search=&schoolid=0&categoryid=&filter=0'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
def sort(n,id):
    if '藝術' in n:#art
        classname(id)
    if '工程' in n:#engineering
        classname(id)
    if 'FUN' in n:#FUN MOOCs
        classname(id)
    if '史地' in n:#polah
        classname(id)
    if '人文' in n:#sp
        classname(id)
    if '資訊' in n:#info_computer
        classname(id)
    if '語言' in n:#lan
        classname(id)
    if '管理' in n:#bs_manage
        classname(id)
    if '數學' in n:#mc_math
        classname(id)
    if '醫療' in n:#mh_mednur
        classname(id)
    if '哲學' in n:#polah_philosophy
        classname(id)
    if '法政' in n:#sp
        classname(id)
    if '心理' in n:#sp_psychology
        classname(id)
    if '科學' in n:#ns
        classname(id)
def classname(id):
    url='https://www.ewant.org/category_course_list.php?sort=startdate&dir=DESC&perpage=200&badgeid=0&categoryid=%s&institutionid=0&search&page=0'%id
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')
    nam=sp.select('div .coursename h4')
    link=sp.select('.courseimage a')
    n=[n.text for n in nam]
    l=[l.get('href') for l in link]
    print(len(n))#課程數量
    for i in range(0,len(n)) :
        print(n[i])#課程名稱
        print(l[i])#課程網址
option=sp.select('#menucategoryid option')
option.remove(option[0])
option.remove(option[0])
course={}
for o in option:
    c=dict([((o.text).replace('\n',""),o.get('value'))])
    course.update(c) 
    print(o.text)
    n=o.text
    for c in course.values():
        #print(c)#類別編號
        sort(n,c)
        #classname(c)