#coding=utf-8
# def函式名稱(參數名稱):
def add(n,m):   
    print(n+m)
add(3,4)
#呼叫函數
def mul(a,b):
    return a*b
print(mul(2,3))

#def函式名稱(*無限/不定參數): 以Tuple處理
def avg(*n):
    sum=0
    for i in n:
        sum+=i
    print(sum/len(n))
avg(3,4,5)
avg(2,4,6,8,10)