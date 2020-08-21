import requests
from bs4 import BeautifulSoup
#coursename=['life_infotech','life_know','life_mark','life_fina','life_man','life_startbusin']
def getcon(a,p):#分類編號,頁數
    for j in range(1, int(p)+1):
        url='https://www.smelearning.org.tw/classes.php?cat1=1000'+a+'&page='+str(j)
        html = requests.get(url)
        sp = BeautifulSoup(html.text, 'html.parser')
        title=sp.select('.sec-classes-list-block .title ')
        link=sp.select('.detail-block .title a ')
        #photo=sp.select('.sec-classes-list-block .img-block ')
        t=[t.text.strip() for t in title]
        l=[l.get('href') for l in link]
        #p=[p.get('href') for p in photo]
        for i in range(0,len(t)):
            print(t[i])#課程名稱
            lk='https://www.smelearning.org.tw/'+str(l[(i*3)])
            print(lk)#課程網址
            #lk='https://www.smelearning.org.tw/'+str(l[(i*3)])
            #print([str(p[(i*3)])#圖片網址
for i in range(2, 8):
    url='https://www.smelearning.org.tw/classes.php?cat1=1000'+str(i)
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')
    title=sp.select('.category-block .title')
    print(title)#分類名稱
    #取得各分類總頁碼
    num=sp.select('.pages-wp a')
    n=[n for n in num]
    page=len(n)-3
    p=n[page].text
    getcon('2','1')
    #getcon(str(i),p)#分類編號,頁數
    


# url='https://www.smelearning.org.tw/classes.php?cat1=1000'+'2'
# html = requests.get(url)
# sp = BeautifulSoup(html.text, 'html.parser')
# num=sp.select('.pages-wp a')
# n=[]
# for c in num:#個別儲存表格進list-->儲存標題
#     n.append(c)
# print(len(n)-3)



#def ceiling(x):
#n = int(x)
#return n if n-1 < x <= n else n+1

# title=sp.select('.category-block .title')
# print(title)
# o=sp.select('.sec-classes-list-block .title ')
# for i in o:
#     print(i.text.strip())

#正確
# url='https://www.smelearning.org.tw/classes.php?cat1=10003&page=8'
# html = requests.get(url)
# sp = BeautifulSoup(html.text, 'html.parser')
# title=sp.select('.category-block .title')
# print(title)
# o=sp.select('.sec-classes-list-block .title ')
# for i in o:
#      print(i.text.strip())

#a=o.select('title')
#print(a)
# a=[]
# for i in o:
#     a.append(i)

#print(sp.text)

#print(option.text.strip())
#option.remove(option[0])
#course={}
#for o in option:
#    c=dict([((o.text).replace('\n',""),o.get('value'))])
#    course.update(c) 