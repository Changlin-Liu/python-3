# -*- encoding:utf-8 -*-
# 导入数据库驱动
import sqlite3
# 连接数据库
conn = sqlite3.connect(r'D:\test.db')
# 创建游标
cursor = conn.cursor()
# 在游标内进行数据库操作
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# rowcount返回插入的行数
print(cursor.rowcount)
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()