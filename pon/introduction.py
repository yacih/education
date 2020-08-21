#cls、cmd+k->清屏
#有順序、可變動的表格 List
[3,4,5]
["Amy","Anson"]
#有順序、不可變動的列表 Tuple
(3,4,5)
("Amy","Anson")
#無順序的 集合Set
{3,4,5}
{"Amy","Anson"}
#鍵與值的配對 字典 Dictionary
{"apple":"蘋果","data":"資料"}
#變數 開頭不可為數字 必須為英文
data=3
#x**y x的y次方

grades=[12,60,75,23,90]
#grades=[1:4] 連續刪除列俵中編號1-4（不包含）的資料
grades+=[83,77]
length=len(grades) #取得列表長度
print(grades)
print(length)

#巢狀列表
data=[[3,5,6],[8,9,3]]
data[0][0:2]=[6,6,6] #將[3,5]換成[6,6,6]
print(data)

#集合的運算
s1={3,4,5}
s2={4,5,6,7}
print(10 in s1)
print(10 not in s1)
print(s1&s2) #交集：兩集合中相同的資料
print(s1|s2) #聯集：兩集合中的所有資料（不重複取）
print(s1-s2) #差集：從s1減去與s1重疊之部分
print(s1^s2) #反交集：兩集和中不重疊的資料
s=set("HELLO")#把字串的字母拆成集合，不重複且無順序
print(s)
dic={"apple":"蘋果","data":"資料"}
print(dic["apple"])
del dic["apple"] #刪除字典中的鍵值對
