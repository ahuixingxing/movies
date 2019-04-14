from flask_wtf import FlaskForm     #表单基类
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from app.models import Admin

class LoginForm(FlaskForm):
    #管理员登录表单
    account=StringField(
        label='帐号',
        validators=[
            DataRequired('请输入帐号!')
        ],
        description='帐号',
        render_kw={
            'class':"form-control",
            'placeholder':"请输入帐号",
            'required':"required"
        }
    )

    pwd=PasswordField(
        label='密码',
        validators=[
            DataRequired('请输入密码!')
        ],
        description='密码',
        render_kw={
            'class':"form-control",
            'placeholder':"请输入密码",
            'required':"required"
        }
    )

    submit=SubmitField(
        label='登录',
        render_kw={
            'class':"btn btn-primary btn-block btn-flat"
        }
    )

    def validate_account(self,field):
        #从Admin数据库中,检测帐号是否存在,如果不存在则在accound.errors中添加错误信息
        account=field.data
        admin_num=Admin.query.filter_by(name=account).count()
        if admin_num==0:
            raise ValidationError('帐号不存在')

class TagForm(FlaskForm):
    name=StringField(
        label='名称',
        validators=[
            DataRequired('标签名称不能为空!')
        ],
        description='标签',
        render_kw={
            'class':"form-control",
            'id':"input_name",
            'placeholder':"请输入标签名称!"
        }
    )
    submit=SubmitField(
        label='提交',
        render_kw={
            'class':"btn btn-primary"
        }
    )