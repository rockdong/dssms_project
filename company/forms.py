#_*_ coding:utf-8 _*_

from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import *
from captcha.fields import CaptchaField


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


class RegisterForm(forms.Form):
    company_name = forms.CharField()
    company_license = forms.CharField()
    corporation = forms.CharField()
    sex = forms.CharField()
    corporation_contact = forms.CharField()
    user_name = forms.CharField()
    password = forms.CharField()
    captcha = CaptchaField()
    # organization = models.ForeignKey(Organization, verbose_name='公司')
    # department = models.ForeignKey(Department, verbose_name='部门')
    # staff_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='姓名')
    #
    # sex = models.CharField(choices=sex_char, max_length=1, null=False, blank=False, verbose_name='性别')
    # # login_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='登陆账号')
    # # password = models.CharField(max_length=50, null=False, blank=False, verbose_name='登陆密码')
    # skills = models.ManyToManyField(Skill, verbose_name='技术/能力')
    # date_join = models.DateField(auto_now_add=True, verbose_name='入职时间')
    # date_out = models.DateField(null=True, verbose_name='离职时间')
