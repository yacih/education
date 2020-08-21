import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
from bs4 import BeautifulSoup
x=input("請輸入專有名詞:")
url = 'http://163.28.84.216/Entry/Detail?title='+x+'&search='+x+'&order=keyword_title'
html = req.get(url)
sp = BeautifulSoup(html.text, 'html.parser')####
dic=sp.find_all('div',{'class':'tab-pane-fade-roydeleted'})#抓表格
form=list()#[1,2,3,4]
source=list()#辭典名稱
name=list()#解釋
for d in dic:#個別儲存表格進list-->儲存表格
    form.append(d)
for f in form:
    source=f.find_all('div',{'class':'col-md-12 border-grey-dark bgGrey-gradient dict-title'})
    name=f.find_all('span',{'class':'withoutRefLink'})
    for s in source:
          if(s.text.strip()=="教育部客家語辭典" or s.text.strip()=="教育部臺灣閩南語常用詞辭典"):
                break
          print(s.text.strip())#印
          for n in name:
                print(n.text.strip())#印
          print() 
    
              
      