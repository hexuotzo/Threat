## -*- coding:utf-8 -*-
from django.contrib import admin
from app1.models import Jihe,Business
#from django import forms
#import datetime
#    
#class CustomForm(forms.ModelForm):
#    class Meta:
#        model = Jihe
#    def clean_start(self):
#        if request.POST:
#            a=request.POST.getlist('city')
#            print a
#        data=City.objects.filter(yewu=self.data['yewu'],cityname=self.data['cityname']) #取出 同城市同业务的数据
#        days=datetime.timedelta(days=3)
#        today = datetime.date.today()
#        date_start=self.data['start'].split('-')
#        date_end=self.data['end'].split('-')
#        syear,smonth,sday=int(date_start[0]),int(date_start[1]),int(date_start[2])
#        eyear,emonth,eday=int(date_end[0]),int(date_end[1]),int(date_end[2])
#        startdate=datetime.date(syear,smonth,sday)
#        enddate=datetime.date(eyear,emonth,eday) #生成开始与结束日期，用于与数据库信息比对
#        if startdate >= enddate:
#            raise forms.ValidationError('开始日期必须早于结束日期')
#        elif startdate - days <= today:
#            raise forms.ValidationError('必须设置3天之后的规则')
#        for i in data:
#            if (i.start <= startdate <= i.end or i.start <= enddate <= i.end or (startdate<i.start and enddate>i.end))and str(i.id) != self.data['tid']:
#                raise forms.ValidationError('同一城市与业务出现时间冲突')
#        return self.cleaned_data["start"]
#            
#        
#    
class JiheAdmin(admin.ModelAdmin):
    list_display = ('city','prov','yewu','start','end')
    search_fields = ['city','prov','yewu']
class BusiAdmin(admin.ModelAdmin):
    list_display = ('yname','yid')
    search_fields = ['yname','yid']
admin.site.register(Jihe,JiheAdmin)
admin.site.register(Business,BusiAdmin)