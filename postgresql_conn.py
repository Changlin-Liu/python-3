import psycopg2
conn = psycopg2.connect(database='orderdb', user='postgres', password='YUTR0-Lew&4-DE74GF-qePi8', host='10.86.0.13')
cur = conn.cursor()
cur.execute('select user_id,create_time from s_order_mj where mobilephone=%s', ['1991581222830'])
value = cur.fetchall()
print(value)
cur.close()
conn.close()