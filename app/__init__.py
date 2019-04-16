# _*_coding:utf-8_*_
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app=Flask(__name__)     #实例化Flask类得到app对象
app.debug=True          #开启调试模式

app.config["SQLALCHEMY_DATABASE_URI"]="mysql+mysqlconnector://root:root@88.10.0.15:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SECRET_KEY"]='b1b7ed6af47d4031acbdeb420658ba84'
#定义文件上传保存的路径,在__init__.py文件所在的目录创建media文件夹,用于保存上传的文件
app.config['UP_DIR']=os.path.join(os.path.abspath(os.path.dirname(__file__)),'static/media/')
app.config['USER_IMAGE']=os.path.join(os.path.abspath(os.path.dirname(__file__)),'static/user/')    #存放用户头像的路径

#定义db对象,实例化SQLAlchemy,传入app对象
db=SQLAlchemy(app)


from app.home import home as home_blueprint     #导入
from app.admin import admin as admin_blueprint


app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

#添加全局404页面
@app.errorhandler(404)
def page_not_found(error):
    return  render_template('404.html'),404