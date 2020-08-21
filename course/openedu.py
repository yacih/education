import requests
from bs4 import BeautifulSoup
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def coursename(id,id2):
    r = requests.get("https://www.openedu.tw/rest/courses/query?&category="+str(id)+"&subcategory="+str(id2), verify=False)
    list_of_dicts = r.json()
    for course in list_of_dicts:
        print(course["courseName"])#課程名稱
        link=str('https://www.openedu.tw/course.jsp?id='+course["id"])
        print(link)
def sort(id,sub,subname):
    if ('宗教'and'哲學'and'神話' in subname):
        print('哲學:'+subname)#
        #coursename(id,sub)
    elif ('心理'and'諮商輔導' in subname):
        print('心理學類:'+subname)#
        #coursename(id,sub)
    elif ('人際關係'and'職場倫理'and'生涯規劃') in subname:
        print('其他社會行為學類:'+subname)#
        #coursename(id,sub)
    elif '數學' in subname:
        print('數學學類:'+subname)#
        #coursename(id,sub)
    elif '物理' in subname:
        print('物理學類:'+subname)#
        #coursename(id,sub)
    elif '化學' in subname:
        print('化學學類:'+subname)#
        #coursename(id,sub)
    elif '天文'and'地球' in subname:
        print('地球科學學類:'+subname)#
        #coursename(id,sub)
    elif '生物'and'人類'and'生命' in subname:
        print('生命科學學類:'+subname)#
        #coursename(id,sub)
    elif '生態'and'能源'and'農業'and'環境' in subname:
        print('環境科學學類:'+subname)#
        #coursename(id,sub)
    elif '電腦'and'通訊' in subname:
        print('電腦運用學類:'+subname)#
        #coursename(id,sub)
    elif '雲端系統'and'資訊安全'and'物聯網' in subname:
        print('網路運用開發學類:'+subname)#
        #coursename(id,sub)
    elif '虛擬實境' in subname:
        print('軟體運用開發學類:'+subname)#
        #coursename(id,sub)
    elif '工程'and'製造'and'應用力學'and'奈米科技'and'電路'and'聲學' in subname:
        print('工程學群:'+subname)#
        #coursename(id,sub)
    elif '都市' in subname:
        print('建築與設計學群:'+subname)#
        #coursename(id,sub)
    elif '管理' in subname:
        print('管理學類:'+subname)#
        #coursename(id,sub)
    elif '醫藥' in subname:
        print('藥學學類:'+subname)#
        #coursename(id,sub)
    elif '營養'and'保健' in subname:
        print('營養學類:'+subname)#
        #coursename(id,sub)
    '''elif id==6:
        print('休憩學類:'+subname)#
        #coursename(id,sub)'''
def subcategory(id):
    r = requests.get("https://www.openedu.tw/rest/subcategories/catId/"+str(id), verify=False)
    list_of_dicts = r.json()
    #print(type(r))
    #print(type(list_of_dicts))
    for category in list_of_dicts:
        sub=category["id"]#二分類id
        #print(str(sub))
        #print(category["name"])#二分類名稱
        sort(id,sub,category["name"])
#        coursename(id,sub)

for i in range(1,11):
#    print("category:"+str(i))#一分類id
    subcategory(i)
#subcategory(2)