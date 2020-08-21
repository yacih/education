#coding=utf-8
# 讀取JSON：
#     import json
#     讀去到的資料=json.load(檔案物件)

# 寫入JSON:
#     import json
#     json.dump(要寫入的資料,檔案物件)

import json #read
with open("myjson.json",mode="r") as myjson:
    data=json.load(myjson)
print(data) #data為字典資料
# print("name:",data["name"])
# print("id:",data["id"])
data["name"]="Ya-Cih" #改變變數中的資料
#把最新的資料複寫回檔案中
with open("myjson.json",mode="w") as myjson:
    json.dump(data,myjson)