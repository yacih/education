'''#通過字典實現
def foo(var):
return {
'a': 1，
'b': 2,
'c': 3,
}.get(var,'error')  #'error'為預設返回值，可自設定
'''   
import sqlite3
db = sqlite3.connect('sort.db')
cursor = db.cursor()
print('Connect ok')
# Create table
cursor.execute('CREATE TABLE info_computer(NAME TEXT PRIMARY KEY NOT NULL,LINK TEXT NOT NULL);')
cursor.execute('CREATE TABLE info_software(NAME TEXT PRIMARY KEY NOT NULL,LINK TEXT NOT NULL);')
cursor.execute('CREATE TABLE info_network(NAME TEXT PRIMARY KEY NOT NULL,LINK TEXT NOT NULL);')
cursor.execute('CREATE TABLE life_license(NAME TEXT PRIMARY KEY NOT NULL,LINK TEXT NOT NULL);')
print('Table created.')
db.commit()

#定義資料庫位置
connect = sqlite3.connect('~/sort.db') # ~代表路徑
c = conn.cursor()
db.close()     #關閉資料庫

with open("data.json",’r’) as f:
       data = json.load(f)
      for line in data[‘data’]:
        sql = "insert into cname(name,id,age) values('%s',%d,%d)" % (line['name'],line['id'],line['age'])
        #注意sql语句中使用了格式化输出的占位符%s和%d来表示将要插入的变量，其中%s需要加引号''
        conn.execute(sql)
        conn.commit()
        #关闭数据库连接
        conn.close()