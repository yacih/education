#判斷式
x=input("請輸入數字1：")#取得字串形式的使用者輸入
x=int(x)#將字串型態轉成數字型態
y=input("請輸入數字2：")
y=int(y)
op=input("請輸入運算：+,-,*,/:")
if op=="+":
    ans=x+y
elif op=="-":
    ans=x-y
elif op=="*":
    ans=x*y   
elif op=="/":
    ans=x/y    
else:
    ans="不支援的運算"
print(ans)
ans=int(ans)
if ans>100:
    print("大於100")
elif ans>50:
    print("介於50與100中間")
elif ans<=50:
    print("小於等於50")
else:
    print(ans)