# -*- coding:utf-8 -*-
from django.db import models
# Create your models here.

class Province(models.Model):
    name = models.CharField('省名称',max_length=100)
    def __unicode__(self):
        return self.name
class Yewu(models.Model):
    name=models.CharField('业务名称',max_length=100)
    def __unicode__(self):
        return self.name
class City(models.Model):
    cityname = models.CharField('市名称',max_length=100)
    prov = models.ForeignKey(Province,verbose_name='省名称')
    yewu = models.ForeignKey(Yewu,verbose_name='业务类型')
    menu = models.BooleanField('勾兑menulog')
    buss = models.BooleanField('勾兑busslog')
    sms = models.BooleanField('勾兑sms')
    user = models.BooleanField('勾兑姓名')  
    qz = models.CharField(blank=True,max_length=5)   
    start = models.DateField('开始日期') 
    end = models.DateField('结束日期')
    def save(self):
        super(City,self).save()
        num_menu,num_buss,num_sms,num_user=0,0,0,0
        if self.menu:num_menu=2
        if self.buss:num_buss=4
        if self.sms:num_sms=8
        if self.user:num_user=16
        qz_num = num_menu + num_buss + num_sms + num_user 
        self.qz =str(qz_num) 
        print self.start,self.end
        super(City,self).save()
    def __unicode__(self):
        return self.cityname
        


    