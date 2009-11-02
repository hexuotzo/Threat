# -*- coding:utf-8 -*-
from django.contrib import admin
from app1.models import Province,City,Yewu
from django import forms
import datetime
    
class CustomForm(forms.ModelForm):
    days=datetime.timedelta(days=3)
    today = datetime.date.today()  
    class Meta:
        model = City
    def clean_start(self):
        data=City.objects.filter(yewu=self.data['yewu'],cityname=self.data['cityname']) #取出 同城市同业务的数据
        days=datetime.timedelta(days=3)
        today = datetime.date.today()
        date_start=self.data['start'].split('-')
        date_end=self.data['end'].split('-')
        syear,smonth,sday=int(date_start[0]),int(date_start[1]),int(date_start[2])
        eyear,emonth,eday=int(date_end[0]),int(date_end[1]),int(date_end[2])
        startdate=datetime.date(syear,smonth,sday)
        enddate=datetime.date(eyear,emonth,eday)           #生成开始与结束日期，用于与数据库信息比对
        if startdate >= enddate:
            raise forms.ValidationError('开始日期必须早于结束日期')
        elif startdate - days <= today:
            raise forms.ValidationError('必须设置3天之后的规则')
        for i in data:
            if (i.start <= startdate <= i.end or i.start <= enddate <= i.end) or (startdate<i.start and enddate>i.end):
                raise forms.ValidationError('同一城市与业务出现时间冲突')
        return self.cleaned_data["start"]
            
        
    
class CityAdmin(admin.ModelAdmin):
    form = CustomForm
    list_display = ('cityname', 'prov','yewu','start','end')
    search_fields = ['cityname','provname']
    fieldsets = [  
        ('选择城市', {'fields': ['prov','cityname','yewu']}),  
        ('约束规则', {'fields': ['menu','buss','sms','user']}), 
        ('时间范围', {'fields': ['start','end']}), 
    ]       
    
admin.site.register(City,CityAdmin)
admin.site.register(Yewu)
admin.site.register(Province)