import mysql.connector
conn = mysql.connector.connect(host='192.168.10.10', \
    user='mysql', password='123456', database='mysql')
cursor = conn.cursor()
# cursor.execute('select name from users where alias=%s', ['hejingqi'])
cursor.execute('select user, password from user')
value = cursor.fetchall()
print(value)
cursor.close()
conn.close()