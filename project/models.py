# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from company.models import Organization, Staff
import os

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

    def __unicode__(self):
        return self.pro_name


class Actor(models.Model):
    """
    Description: 项目参与者
    """
    pro = models.ForeignKey(Pro, verbose_name='项目')
    pro_actors = models.ManyToManyField(Staff, verbose_name='项目参与者')

    class Meta:
        verbose_name='项目参与者'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        msg = "项目名称 : " + self.pro.pro_name + " > 项目参与者 [ "
        isFirst = True
        for act in self.pro_actors.all():
            if not isFirst :
                msg += ","
            msg += act.staff_name
        msg += " ]"
        return msg


class ProFlowBlank(models.Model):
    """
    Description: 项目流程块，比如：意向，设计，施工，售后服务
    """
    pro = models.ForeignKey(Pro, verbose_name='项目')
    pro_flow_name = models.CharField(max_length=50, verbose_name='项目流程块')

    class Meta:
        verbose_name='项目流程块'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return pro.pro_name + " > " + pro_flow_name


class PlanFlow(models.Model):
    """
    Description: 项目计划时间
    """
    pro_flow_blank = models.ForeignKey(ProFlowBlank, verbose_name='项目流程块')
    pre_st_date = models.DateField(auto_now_add=False ,null=False, blank=False, verbose_name='项目预计开始时间')
    pre_ed_date = models.DateField(auto_now_add=False ,null=False, blank=False, verbose_name='项目预计结束时间')

    class Meta:
        verbose_name='项目计划时间'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.pro_flow_blank.pro.pro_name + " > [ 预计开始时间:" + pre_st_date + ", 预计结束时间:" + pre_ed_date + " ]"


class Actual(models.Model):
    """
    Description: 项目实际时间
    """
    pro_flow_blank = models.ForeignKey(ProFlowBlank, verbose_name='项目流程块')
    act_st_date = models.DateField(auto_now_add=False ,null=False, blank=False, verbose_name='项目实际开始时间')
    act_ed_date = models.DateField(auto_now_add=False ,null=False, blank=False, verbose_name='项目实际结束时间')

    class Meta:
        verbose_name='项目实际时间'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.pro_flow_blank.pro.pro_name + " > [ 实际开始时间:" + pre_st_date + ", 实际结束时间:" + pre_ed_date + " ]"


class Action(models.Model):
    """
    Description: 项目流程块下面的行为，如：现场勘查，设计提案，装修工程预算报价
    """
    action_types = (
        ('0', '一般行为'),
        ('1', '设计图'),
        ('3', '报价'),
        ('4', '合同'),
    )

    pro_flow_blank = models.ForeignKey(ProFlowBlank, verbose_name='项目流程块')
    action_content = models.CharField(max_length=50, verbose_name='行为')
    action_type = models.CharField(choices=action_types, max_length=20, verbose_name='行为类型')

    class Meta:
        verbose_name='行为'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.pro_flow_blank.pro_flow_name + " > " + self.pro_flow_blank.pro_flow_name




'''

class Pic(models.Model):
    """
    Description: 图类
    """
    pro_flow_blank = models.ForeignKey(ProFlowBlank, verbose_name='项目流程块')
    # 公司/项目/
    img = models.ImageField(upload_to='%s/%s/', \
                        blank=False, null=False, verbose_name='设计图')
    is_confirm = models.BooleanField(default=False, verbose_name='确认信息')
    pic_date_publish = models.DateField(auto_now_add=True ,null=False, blank=False, verbose_name='设计图发布时间')

    class Meta:
        verbose_name='设计图'
        verbose_name_plural=verbose_name


    def __unicode__(self):
        return pro_flow_blank.pro_flow_name + " > " + img + " : " + pic_date_publish


class Process(models.Model):
    """
    Description: 工序定义，用于定义施工内容
    """
    org = models.ForeignKey(Organization, verbose_name='公司')
    process_name = models.CharField(max_length=20, primary_key=True, verbose_name='工序名称')

    class Meta:
        verbose_name='工序'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.process_name


class Subitem(models.Model):
    """
    Description: 子项目，属于施工类型
    """
    pro_flow_blank = models.ForeignKey(ProFlowBlank, verbose_name='项目流程块')
    processes = models.ManyToManyField(Process, verbose_name='工序')
    con_st_date = models.DateField(auto_now_add=True ,null=False, blank=False, verbose_name='子项目开始时间')

    class Meta:
        verbose_name='子项目'
        verbose_name_plural=verbose_name

'''
# class ProTemplate(models.Model):
#     """
#     Description: 项目模板
#     """
    

#     class Meta:
#         pass