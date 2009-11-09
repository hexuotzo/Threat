# -*- coding:utf-8 -*-
from django.db import models
# Create your models here.

#class Province(models.Model):
#    num = models.IntegerField('省编码')
#    name = models.CharField('省名称',max_length=100)
#    class Meta:
#        verbose_name = u"省份"
#        verbose_name_plural = u"省份管理"
#    def __unicode__(self):
#        return '%s--ID:%s'% (self.name,self.num)
#class City(models.Model):
#    name=models.CharField('市名称',max_length=100)
#    num= models.IntegerField('市ID')
#    prov= models.ForeignKey(Province)
#    class Meta:
#        verbose_name = u"城市"
#        verbose_name_plural = u"城市管理"        
#    def __unicode__(self):
#        return '%s--ID:%s'% (self.name,self.num)
class Jihe(models.Model):
    city = models.CharField('市名称',max_length=100)
    cid = models.CharField('市编码',max_length=100)
    prov = models.CharField('市名称',max_length=100)
    pid = models.CharField('市编码',max_length=100)    
    yewu = models.CharField('业务类型',max_length=100)
    sms = models.CharField('勾兑sms',max_length=50)   #稽核值：2
    user = models.CharField('勾兑姓名',max_length=50)  #稽核值：2   
    qz = models.IntegerField('权值')
    start = models.DateField('开始日期')
    end = models.DateField('结束日期')
    class Meta:
        verbose_name = u"稽核"
        verbose_name_plural = u"稽核管理"   
           
    def __unicode__(self):
        return self.city
    