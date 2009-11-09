# -*- coding:utf-8 -*-
from django.db import models
# Create your models here.
class Jihe(models.Model):
    city = models.CharField('市名称',max_length=100)
    cid = models.CharField('市编码',max_length=100)
    prov = models.CharField('省名称',max_length=100)
    pid = models.CharField('省编码',max_length=100)    
    yewu = models.CharField('业务类型',max_length=100)
    yid = models.CharField('业务编码',max_length=100)
    sms = models.CharField('勾兑sms',max_length=50)   #稽核值：2
    user = models.CharField('勾兑姓名',max_length=50)  #稽核值：4   
    qz = models.IntegerField('权值')
    start = models.DateField('开始日期')
    end = models.DateField('结束日期')
    class Meta:
        verbose_name = u"稽核"
        verbose_name_plural = u"稽核管理"  
    def __unicode__(self):
        return "%s--%s" % (self.city,self.yewu)
class Business(models.Model):
    yid = models.CharField('业务编码',max_length=100)
    yname = models.CharField('业务名称',max_length=100)
    class Meta:
        verbose_name = u"业务"
        verbose_name_plural = u"业务管理"
    def __unicode__(self):
        return self.yname