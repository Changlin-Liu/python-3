import mysql.connector
conn = mysql.connector.connect(user='root', password='root', database='zabbix')
cursor = conn.cursor()
cursor.execute('select name from users where alias=%s', ['hejingqi'])
value = cursor.fetchall()
print(value)
cursor.close()
conn.close()