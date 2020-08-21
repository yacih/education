# -*- coding: UTF-8 -*-
#網路連線程式、公開資料串連
# import urllib.request as ur
# src="http://library.mcu.edu.tw"
# with ur.urlopen(src) as response:
#     data=response.read().decode("utf-8")    #取得銘傳大學圖書館網站的原始碼(HTML、CSS、JS)
# print(data)

import urllib.request as ur
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
src="https://www.nlpi.edu.tw/opendata/da08aaaf-7edd-461d-a645-3039f840a1a8?format=json"
with ur.urlopen(src) as response:
    libinf=json.load(response)    #利用json模組處理json資料格式
with open("libinf.txt",mode="w") as file:
    for libname in libinf:
        file.write(libname["圖書館名稱"]+"\n")

# print(libname) 
# libinf=data['result']['results']
# print(data) 
   