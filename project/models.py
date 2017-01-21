# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from company.models import Organization, Staff

# Create your models here.

class Pro(models.Model):
    """
    Description: 项目
    """
    org = models.ForeignKey(Organization, verbose_name='公司')
    pro_name = models.CharField(max_length=50, verbose_name='项目编号')
    
    class Meta:
        verbose_name='项目'
        verbose_name_plural=verbose_name


class Actor(models.Model):
    """
    Description: 项目参与者
    """
    pro = models.ForeignKey(Pro, verbose_name='项目')
    pro_actor = models.ManyToManyField(Staff, verbose_name='项目参与者')

    class Meta:
        verbose_name='项目参与者'
        verbose_name_plural=verbose_name


class Plan(models.Model):
    """
    Description: 项目计划时间
    """
    pro = models.ForeignKey(Pro, verbose_name='项目')
    pre_st_date = models.DateField(auto_now_add=False ,null=False, blank=False, verbose_name='项目预计开始时间')
   	pre_ed_date = models.DateField(auto_now_add=False ,null=False, blank=False, verbose_name='项目预计结束时间')

    class Meta:
        verbose_name='项目计划时间'
        verbose_name_plural=verbose_name


class Actual(models.Model):
    """
    Description: 项目实际时间
    """
    pro = models.ForeignKey(Pro, verbose_name='项目')
    act_st_date = models.DateField(auto_now_add=False ,null=False, blank=False, verbose_name='项目实际开始时间')
   	act_ed_date = models.DateField(auto_now_add=False ,null=False, blank=False, verbose_name='项目实际结束时间')

    class Meta:
        verbose_name='项目实际时间'
        verbose_name_plural=verbose_name