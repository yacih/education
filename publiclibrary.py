import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib
#import requests
import bs4 as bs
url="http://book.tpml.edu.tw/webpac/bookSearchList.do?searchtype=simplesearch&execodeHidden=true&execode=&authoriz=1&search_field=TI&search_input=%E5%B0%8F%E7%8E%8B%E5%AD%90"
request=urllib.request.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
})
html = urllib.request.urlopen(request)
# with req.urlopen(request) as response:
#     data=response.read().decode("utf-8") 
# content=
sp=bs.BeautifulSoup(html.txet, "html.parser")
ans=sp.select("html head title ")
ans = sp.find_all('a')

print(ans)
# container=soup.select("h3 a)
# titles = root.find_all("div", class_="tablesorter")
# print(titles.a.target)
