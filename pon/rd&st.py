#coding=utf-8
import random
import statistics as st #st為statistics之別名
#從列表中隨機選取1個資料
random.choice([0,1,5,8])
#重列表中隨機選取兩個資料
data=random.sample([0,1,5,8],2)
print(data)
#將列表的資料「就地」隨機調換順序
data=[0,1,5,8]
random.shuffle(data)
print(data) 
#隨機亂數：取得0.0～1.0之間的隨機亂數
random.random()
random.uniform(0.0,1.0)
#常態分配亂數：取得平均數100＆標準差10的
random.normalvariate(100,10)
#平均數
data=st.mean([1,4,6,9])
print(data)
#中位數
st.median([1,4,6,9])
#標準差
st.stdev([1,4,6,9])

