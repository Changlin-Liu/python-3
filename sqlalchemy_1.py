from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'new'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

TEST_URL = 'postgresql://postgres:123456@127.0.0.1:5432/test'
engine = create_engine(TEST_URL)
DBSession = sessionmaker(bind=engine)
"""
session = DBSession()
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()
"""
session_2 = DBSession()
user = session_2.query(User).filter(User.id=='1').one()
print('type:', type(user))
print('name:', user.name)
session_2.close()