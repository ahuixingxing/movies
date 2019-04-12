# _*_coding:utf-8_*_
from flask import Flask

app=Flask(__name__)     #实例化Flask类得到app对象
app.debug=True          #开启调试模式

from app.home import home as home_blueprint     #导入
from app.admin import admin as admin_blueprint


app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')


#定义连接的数据库
#app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:root@88.10.0.15:3306/movie"

#如果设置成True(默认情况),Flask-SQLAlchemy将会追踪对象的修改并且发送信号
#这需要额外的内存,如果不必要的可以禁用
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

#定义secret_key
#app.config['SECRET_KEY']="6bd749587aad49399f674b202a07d56f"

#db=SQLAlchemy(app)