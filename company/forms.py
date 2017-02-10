#_*_ coding:utf-8 _*_

from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import *


class CompanyLoginForm(forms.Form):
    """
    Description: 公司用户登陆界面
    """
    companyname = forms.CharField(label="", widget=BootstrapTextInput(attrs={"placeholder":"公司名", "required":"必须输入公司名", "size":30}),
                              max_length=50,error_messages={"required": "公司名不能为空",})
    username = forms.CharField(label="", widget=BootstrapTextInput(attrs={"placeholder":"用户名", "required":"必须输入用户名", "size":30}),
                              max_length=50,error_messages={"required": "用户名不能为空",})
    password = forms.CharField(label="", widget=BootstrapPasswordInput(attrs={"placeholder":"密码", "required":"必须输入密码", "size":30}),
                              max_length=20,error_messages={"required": "密码不能为空",})