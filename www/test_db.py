# coding:utf-8

from models import User, Blog, Comment,Accounts
from transwarp import db
import ConfigParser
import os
import logging
import time
cf = ConfigParser.ConfigParser()
path = os.path.dirname(os.path.abspath(__file__))
cf.read(path+r'\db1.cfg')
secs = cf.sections()
host = cf.get('db', 'host')
user = cf.get('db', 'username')
password = cf.get('db', 'passwd')
database = cf.get('db', 'database')
port = int(cf.get('db', 'port'))
db.create_engine(user=user,password=password,database=database,host=host,port=port)
logging.basicConfig(level=logging.DEBUG)
# 添加
# u = User(name='Test', email='test@example5.com',password='1234567',image='about:blank',admin = 0)
# u.insert()
# 查找
# u1 = User.find_first('select * from users where admin = ?',1)
# u1 = User.find_first('where admin = ?',0)
# blogs = Blog.find_all("where 1=1")
# print blogs
# name='confluence'
# blogs = Accounts.find_all('where name=?',name)
# print blogs
# account_insert = Accounts(name='学习资料', url='192.168.50.248', accname='cmmi', passwd='cmmi', admin=1, detail='常用软件')
# account_insert.insert()

account = Accounts.get('001548073299212d6600111951d49cf832fe1b61202cad8000')
account.delete()
# print u1
# 删除
# u1.delete()












