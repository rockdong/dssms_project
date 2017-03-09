# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Organization(models.Model):
    """
    Description: 公司，每个公司注册必需提供所有的信息，信息需要复核，无误后才可以进入平台。
    """
    company_name = models.CharField(null=False, max_length=50, primary_key=True, verbose_name='企业名称')
    # company_license = models.ImageField(upload_to='license/%s/', \
    #                     blank=False, null=False, verbose_name='营业执照')
    corporation = models.CharField(max_length=20, null=False, blank=False, verbose_name='法人代表')
    corporation_contact = models.CharField(max_length=20, null=False, blank=False, verbose_name='联系方式')
    date_regedit = models.DateTimeField(auto_now=True, verbose_name='注册时间')

    class Meta:
        verbose_name = '企业'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.company_name


class Department(models.Model):
    """
    Description: 部门，用来定义公司的组织架构，目前只支持一层架构
    """
    organization = models.ForeignKey(Organization, verbose_name='公司')
    department_name = models.CharField(max_length=50, null=False, blank=False, primary_key=True, verbose_name='部门名称')

    class Meta:
        verbose_name='部门'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.department_name


class Duty(models.Model):
    """
    Description: 部门下面的职位
    """
    organization = models.ForeignKey(Organization, verbose_name='公司')
    department = models.ForeignKey(Department, verbose_name='部门')
    duty_name = models.CharField(max_length=20,verbose_name='职位名称')

    class Meta:
        verbose_name='职位名称'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.duty_name


class Skill(models.Model):
    """
    Description: 技术/能力，用于定义员工技能
    """
    organization = models.ForeignKey(Organization, verbose_name='公司')
    skill_name = models.CharField(max_length=20, primary_key=True, verbose_name='技术')

    class Meta:
        verbose_name='技术/能力'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.skill_name


class Staff(AbstractUser):
    """
    Description: 公司成员信息
    """
    sex_char = (
        ('M', '男'),
        ('F', '女')
    )

    organization = models.ForeignKey(Organization, verbose_name='公司')
    department = models.ForeignKey(Department, verbose_name='部门')
    duty = models.ForeignKey(Duty, verbose_name='职位')
    staff_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='姓名')
    
    sex = models.CharField(choices=sex_char, max_length=1, null=False, blank=False, verbose_name='性别')
    # login_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='登陆账号')
    # password = models.CharField(max_length=50, null=False, blank=False, verbose_name='登陆密码')
    skills = models.ManyToManyField(Skill, verbose_name='技术/能力')
    date_join = models.DateField(auto_now_add=True, verbose_name='入职时间')
    date_out = models.DateField(null=True, verbose_name='离职时间')

    class Meta:
        verbose_name='公司成员'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.staff_name