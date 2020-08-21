
import sqlite3
db = sqlite3.connect('TEST.db')
cursor = db.cursor()
print('Connect ok')

# Create table
cursor.execute(
'''CREATE TABLE HUMAN
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL);''')
print('Table created.')
db.commit()

# Insert
cursor.execute('''INSERT INTO HUMAN (ID,NAME,AGE) VALUES (1, 'Clay', 25)''')
cursor.execute('''INSERT INTO HUMAN (ID,NAME,AGE) VALUES (2, 'Wendy', 16)''')
db.commit()
print('Insert ok')

# Select
results = cursor.execute('''SELECT * FROM HUMAN''')
for item in results:
    print(item)

# Update
results = cursor.execute('''UPDATE HUMAN set AGE = 26 WHERE ID = 1''')
db.commit()

# Select
results = cursor.execute('''SELECT * FROM HUMAN''')
for item in results:
    print(item)

# Delete
cursor.execute('''DELETE FROM HUMAN WHERE ID = 2''')
db.commit()

# Select
results = cursor.execute('''SELECT * FROM HUMAN''')
for item in results:
    print(item)

db.close()     #關閉資料庫