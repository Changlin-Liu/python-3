import sqlite3
conn = sqlite3.connect(r'D:\learn\python\test.db')
cursor = conn.cursor()
cursor.execute('select * from user;')
value = cursor.fetchall()
cursor.close()
conn.close()
print(value)
