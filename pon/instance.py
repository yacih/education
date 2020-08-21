# class IO類別名稱(首字英文大寫):
    # supportedSrcs=["console","file"]定義封裝的變數
    # def read(src):定義封裝的函數
    #     print("Read from",src) 

#Point 實體物件的設計：平面座標上的點
class Point:
    def ___init__(self,x,y):
        self.x=x
        self.y=y
p1=Point(7,8)
print(p1.x,p1.y)
p2=Point(5,6)
print(p2.x,p2.y)
# 實體物件的設計
class FullName:
    def __init__(self,first,last):
        self.first=first
        self.last=last
n1=FullName("Y.C.","Hsieh")
print(n1.first,n1.last)
n2=FullName("B.H.","YA")
print(n2.first,n2.last)

class File:
    def ___init__(self,name):
        self.name=Name
        self.file=None #尚未開啟檔案：初期事None
    def open(self):
        self.file=open(self.name,mode="r")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)
#讀取第二個檔案
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)