import requests
from bs4 import BeautifulSoup
def sort(cg,subcg):
    if cg=='163': 
        if subcg=='205':
            print('英語文學類')#lan_english
            runall(cg,subcg)
        elif subcg=='206':
            print('日語文學類')#lan_japanese
            runall(cg,subcg)
        elif subcg=='207':
            print('東方語文學類')#lan_chinese
            runall(cg,subcg)
        elif subcg=='208':
            print('歐語文學類')#lan_european
            runall(cg,subcg)    
        elif subcg=='406' :
            print('東方語文學類')#lan_chinese
            runall(cg,subcg)
        elif subcg=='407' :
            print('東方語文學類')#lan_chinese
            runall(cg,subcg)
        else:
            print('漢語文學類')#lan_chinese
            runall(cg,subcg)
    if cg=='164': 
        if subcg=='217':
            print('電腦運用學類')#info_computer
            runall(cg,subcg)
        elif subcg=='218':
            print('數學學類')#mc_math
            runall(cg,subcg)
        elif subcg=='219':
            print('物理學類')#mc_physical
            runall(cg,subcg)
        elif subcg=='220':
            print('化學學類')#mc_chemistry
            runall(cg,subcg)
        elif subcg=='223':
            print('建築與設計學群')#ad
            runall(cg,subcg)
        elif subcg=='224':
            print('醫學與護理學類')#mh_mednur
            runall(cg,subcg)    
        elif subcg=='225':
            print('生命科學學類')#ns_lifes
            runall(cg,subcg)
        elif subcg=='441':
            print('心理學類')#sp_psychology
            runall(cg,subcg)
        else:
            print('工程學群')#engineering
            runall(cg,subcg)
    if cg=='165': 
        if subcg=='227':
            print('中國文學學類')#polah_chinese
            runall(cg,subcg)
        elif subcg=='228':
            print('歷史學類')#polah_history
            runall(cg,subcg)
        else:
            print('哲學學類')#polah_philosophy
            runall(cg,subcg)
    if cg=='166': 
        if subcg=='233':
            print('經濟學類')#bs_business
            runall(cg,subcg)
        else:
            print('管理學類')#bs_manage
            runall(cg,subcg)
    if cg=='167': 
       print('財政學類')#bs_financial
       runall(cg,subcg)
    if cg=='168': 
        if subcg=='242':
            print('電腦運用學類')#info_computer
            runall(cg,subcg)
        elif subcg=='243':
            print('電腦運用學類')#info_computer
            runall(cg,subcg)
        elif subcg=='246':
            print('網路應用開發學類')#info_network
            runall(cg,subcg)  
        else:
            print('軟體應用開發學類')#info_software
            runall(cg,subcg)  
    if cg=='169': 
       print('法律學類')#sp_legal
       runall(cg,subcg)
    if cg=='170': 
       print('公共行政與社會工作學類')#sp_ps
       runall(cg,subcg)
    if cg=='171': 
       print('建築與設計學群')#ad
       runall(cg,subcg)
    if cg=='172': 
       print('音樂學類')#art_music
       runall(cg,subcg)
    if cg=='173': 
       print('美術學類')#art_paint
       runall(cg,subcg)
    if cg=='174':
        if subcg=='272':
            print('心理學類')#sp_psychology
            runall(cg,subcg)
        else:
            print('體育學類')#re_pe
            runall(cg,subcg)
    if cg=='175':
        if subcg=='276':
            print('體育學類')#re_pe
            runall(cg,subcg)
        elif subcg=='277':
            print('休憩學類')#re_rest
            runall(cg,subcg)
        elif subcg=='280':
            print('醫學與護理學類')#mh_mednur
            runall(cg,subcg)
        else:
            print('管理學類')#bs_manage
            runall(cg,subcg)
    if cg=='176':
        print('教育學類')#sp_educate
        runall(cg,subcg)   
    if cg=='177':
        print('證照檢定')#life_license
        runall(cg,subcg)
def runall(cg,subcg):
    url='https://cell.moe.edu.tw/Guests/CourCg.aspx?cg='+cg+'&subcg='+subcg
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')####   
    name=sp.select('a.hp3')
    na=[na.text for na in name]
    lk=[lk.get('href') for lk in name]
    #print(len(na))
    for i in range(0,len(na)):
        print(na[i])
        print('https://cell.moe.edu.tw/Guests/'+lk[i])
def courseid(id):
    url = 'https://cell.moe.edu.tw/Guests/CourCg.aspx?cg='+id
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')
    coursess_text = sp.find_all('select')[2]
    coursesss=sp.select('#MainContent_ddlSubcg option')
    coursesss.remove(coursesss[0])
    ccname={}
    for o in coursesss:
        r=dict([((o.text).replace('\n',""),o.get('value'))])
        ccname.update(r)
    for s in ccname.values():
        #print('第二層:'+s)
        #runall(cc,s)
        sort(cc,s)
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
#    print(c.text.strip())
for cc in cname.values(): 
    if cc<'178':
        #print('（第一層）'+cc)#分類編號
        courseid(cc)