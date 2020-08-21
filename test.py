# words={
#     'yaci':'a',
#     'penny':[
#         'a','b','c'
#     ],
#     'rick':{
#         'name':'rick',
#         'gender':"boy",
#         'age':[
#             'aaa','bbb','ccc'
#         ]
#     }
# }
# for word in range(len(words['penny'])):
#     print(words['penny'][word])

# rick=words['rick']['age']
# for i in range(len(rick)):
#     print(rick[i])

# num=words['rick']['age']
# for i in range(len(num)):
#     print(num[i])


'''
url=requests.get("https://www.openedu.tw/rest/subcategories/catId/1")
list_of_dicts = url.json()
list=eval(url.text)
for dict in list:
    listvalues=list(dict.values())
    print(listvalues)
'''
# import urllib.request as ur
# import json
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# src="https://www.openedu.tw/rest/subcategories/catId/1"
# with ur.urlopen(src) as response:
#     #libinf=json.load(response)   
#     data=response.read().decode("utf-8")
#     #i=data["id"]
# print(data)
# for i in data:
#   print(i["id"])

# import json 
# from urllib import request
# import pandas as pd
# url = 'https://works.ioa.tw/weather/api/weathers/289.json'
# json_data = request.urlopen(url).read().decode("utf-8")
# json_data = json.loads(json_data)
# frame = pd.DataFrame.from_dict(json_data)
# print(frame)

'''
import requests
r = requests.get("https://www.openedu.tw/rest/subcategories/catId/1", verify=False)
list_of_dicts = r.json()
print(type(r))
print(type(list_of_dicts))
for i in list_of_dicts:
    print(i["id"])
'''

'''
import requests
import urllib.request as req
import urllib
url=""
with req.urlopen(url) as response:
    data=response.read()
print(data)
'''

'''
a=22.7

if a%2==1 or a%2==0:
    print("整数")
else:
    print("不是整数")
'''

'''
import requests
from bs4 import BeautifulSoup
def page(a):
    url = "https://www.tocec.org.tw/web/school_results.jsp?s_group_id=9"
    payload = 'page_num='+a
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID=E07450B9DA577F553F651C344BD958DE'}
    html = requests.request("POST", url, headers=headers, data = payload)
    sp = BeautifulSoup(html.text, 'html.parser')
    nam=sp.select('tbody a')
    for a in nam:
        print(a.text.strip())
for i in range(1,6):
    print(i)
    page(str(i))


for j in range(1, 4):
    pp=str(j)
    print(pp)
    url='https://www.tocec.org.tw/web/school_results.jsp?s_group_id=1'
    payload = 'page_num=2'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    html = requests.request("POST", url, headers=headers, data = payload)
    sp = BeautifulSoup(html.text, 'html.parser')####
    nam=sp.select('tbody a')
    for a in nam:
        print(a.text.strip())
'''
'''
＊網路連線＊
<載入模組>
import urllib.request

<下載特定網址資料>
import urllib.request as request
with request.urlopen(網址) as response:
  data = response.read()
print(data)

公開資料：
適合的資料來源：台北市政府公開資料
確認資料格式：  JSON, CSV, 或其他格式
解讀JSON格式： 使用內建的json模組
'''

'''
# 網路連線
import urllib.request as request
src = "https://www.ntu.edu.tw"
with request.urlopen(src) as response:
  # 取得台灣大學網站的原始碼
  # .decode("utf-8") => 顯示中文，不然本來是亂碼
  data = response.read().decode("utf-8")
print(data)
#>>> 跑出NTU的html

# 串接、擷取公開資料
# data.taipei
import urllib.request as request
import json
src = "資料網址請複製貼上"
with request.urlopen(src) as response:
  data = json.load(response) # 利用 json 模組處理 json 資料格式
print(data)
#>>> 一堆
# 將公司名稱列表出來
clist = data["result"]["results"]
for company in clist:
  print(company["公司名稱"])

# 檔案寫入公司名稱+\n換行符號
clist = data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
  for company in clist:
    file.write(company["公司名稱"]+"\n")
'''
'''
import requests
from bs4 import BeautifulSoup

url='https://www.smelearning.org.tw/classes.php?cat1=10003&page=8'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
o=sp.select('.sec-classes-list-block .title ')
for i in o:
  ii=i.text.strip()
  print(ii)
  for link in o.find_all('a'):
    print(link.get('href'))
'''

'''for t2 in t1:
  t3 = t2.get('href')
  link.append(t3)
for i in range(len(link)):
  print(i)
  print(":")
  print(link[i])'''

'''
from urllib.request import urlopen#用於獲取網頁
from bs4 import BeautifulSoup#用於解析網頁

html = urlopen('https://www.douban.com/')
bsObj = BeautifulSoup(html, 'html.parser')
t1 = bsObj.find_all('a')
for t2 in t1:
    t3 = t2.get('href')
    print(t3)
    '''

'''
import requests
from bs4 import BeautifulSoup
url='https://www.smelearning.org.tw/classes.php?cat1=10002&page=2'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
o=sp.select('.sec-classes-list-block .title ')
link=sp.select('.detail-block .title')
#for i in o:
#  print(i.text.strip())
for j in link:
  print(j.text.strip())
  print(j.get('href'))
'''

#t1 = o.find_all('a')
#for t2 in t1:
#   t3 = t2.get('href')
#   print(t3)



'''for i in o:
  ii=i.text.strip()
  print(ii)
  t1 = o.select('a')
  for t2 in t1:
    t3 = t2.get('href')
    print(t3)


t1 = sp.select('a')
for t2 in t1:
    t3 = t2.get('href')
    print(t3)'''

