import requests
from bs4 import BeautifulSoup
#x=input("請輸入書名:")
url = 'https://hylib.typl.gov.tw/bookSearchList.do?searchtype=simplesearch&execodeHidden=true&execode=&authoriz=1&search_field=TI&search_input='+x+'&searchsymbol=hyLibCore.webpac.search.common_symbol&keepsitelimit=&resid=188942689&nowpage=1#searchtype=simplesearch&execodeHidden=true&execode=&authoriz=1&search_field=TI&search_input='+x+'&searchsymbol=hyLibCore.webpac.search.common_symbol&keepsitelimit=&resid=188942689&nowpage=1''
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
str1=sp.find('a')
#str2=sp.find_all('div',{'class':'booklist'})
#str3=min(len(str1),len(str2))
print(str1)
#for i in str1:
    #print(i.text)
    