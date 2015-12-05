from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'new'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 连接表示方法：数据库类型+数据库驱动名称://用户名:密码@ip:port/数据库名
TEST_URL = 'postgresql://postgres:123456@127.0.0.1:5432/test'
# 初始化数据库连接
engine = create_engine(TEST_URL)
# 创建session类型
DBSession = sessionmaker(bind=engine)
"""
session = DBSession()
# 创建user对象
new_user = User(id='5', name='Bob')
# 添加user对象到session
session.add(new_user)
session.commit()
session.close()
"""
session = DBSession()
session.execute("insert into new values(3, 'mengke')")
session.commit()
session.close()