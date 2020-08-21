#連線到特定網址，抓取資料
#解析資料，取得所需之部分

#步驟一：抓取PTT電影版的網頁原始碼（HTML）
#因為是mac電腦，所以先執行下列兩行程式碼才有辦法抓到網路上資料
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Step1. 先import urllib.request這個內建的封包，以執行接下來的動作，並且取名為req，以方便之後操作
import urllib.request as req
url="https://www.ptt.cc/bbs/part-time/index.html"
#建立一個request物件，附加Request Headers的資訊——為了讓我們看起來更像一個真正的使用者（不然PTT不會讓我們抓資料）
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
})
# Step2. 使用with request.urlopen(網址)連上網路，並將其重新取名為response，最後使用read()函數，將網頁結果放入data中
#原本req.urlopen的括號內會放網址，但為了讓我們更像一般使用者，這邊放入剛剛建立的物件
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")  #取得網頁原始碼並用decode("uyf-8")來翻譯成中文（解碼）
print(data) #取得PTT打工版的網頁原始碼

#步驟二：解析原始碼，取得每篇文章的標題
#使用第三方套件：beautifulsoup4/直接在終端機打pip install beautifulsoup4
    #debug：因為是用macbook，下載BS4相對麻煩些：
    # Step1.將 "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.pysudo python get-pip.py" 貼上終端機
    # Step2.將 "sudo python get-pip.py"貼上終端機。此處將會要求輸入電腦密碼
    # Step3.下載pip，將"sudo easy_install pip"貼上終端機
    # Step4.下載BS4，將"pip install beautifulsoup4"貼上終端機
    # Step5.再次下載BS4，將"pip3 install beautifulsoup4"貼上終端機

# 載入 bs4 套件
import bs4
#利用上方載入套件做解析：變數data是剛在網路上抓到的資料，丟給Beautifulsoup4，他會幫我們用html解析。並用root代表整份網頁
root=bs4.BeautifulSoup(data, "html.parser")
#印出網頁，並解透過"."來操作要抓取的東西
 #print(root.title) #.title：抓取網頁標題 <title> 以及 </titl3> 分別代表開始與結束。
 #print(root.title.string) #.title.string：抓取標籤內的文字(不會再顯示印出上方時句首句末會出現的<title>以及</titl3>)
#觀察原始碼，看看我們要找的資料有無特別之處
#舉例：在PTT打工版中，找的每一則文章標題，在原始碼中都會先被<a>夾住，再被<div>包住。這就是特色！ 
#使用 BS4 中強大的套件：
#下方因為class是python的保留字，程式中不能使用。所以BeautifulSoup就選擇使用class_來篩選標籤中的class屬性

#使用".find"可以幫助我們找到符合"一個"以下條件的東西
    #titles = root.find("div", class_="title")   #尋找class="title"的div標籤
    #print(titles)   #印出剛剛上面找到的標籤。titles代表上面找到的div標籤
    #print(titles.a.string)  #".a"為剛剛找到的那個div標籤底下的<a>裡面的東西；".string"為抓取前面"titles.a"抓到的東西的文字
 
#使用".find_all"可以幫助我們找到「全部」符合以下條件的東西
titles = root.find_all("div", class_="title")
#print(titles)
#做完上面動作之後，會發現印出來的資料是一個列表的形式，因此嘗試使用for迴圈將標題資料抓出來
for title in titles:
    if title.a != None: #因為可能會有內文被刪除的狀況，如果發生則div下就不會有<a>標籤。使用這個判斷式判斷此狀況是否發生
        print(title.a.string) # 如果「不是None」這件事發生，則印出標題（"titles.a" 抓到的東西的文字）
