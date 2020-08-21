#coding=utf-8
#檔案物件＝open(檔案路徑,mode=開啟模式)
#讀取模式r;寫入模式w;讀寫模式r+
#寫入文字：檔案物件.write("範例文字\n")
#讀取全部文字：檔案物件.read()
# 關閉檔案
# 基本語法：檔案物件.close()
# 自動、安全的關閉檔案：
#     with open(檔案路徑,mode=開啟模式) as 檔案物件:
#         讀取或寫入檔案的程式
#第一總方式
file=open("data.txt",mode="w")  #開啟
file.write("hello \n你好")    #操作
file.close()    #關閉

#第二種方式（會自動關閉檔案）
# with open("data.txt",mode="w") as file: 
#     file.write("hello \n你好")
with open("data.txt",mode="w") as file: #儲存檔案
    file.write("5 \n3")

sum=0
with open("data.txt",mode="r") as file:  #讀取檔案
     for line in file:
        sum+=int(line)  #將每行讀取到的資料轉成int並加總
    #一次讀取一行：
        #for變數in檔案物件：
        #從檔案依序讀取每行文字到變數中
print(sum)
    # data=file.read()
    # print(data)
 


