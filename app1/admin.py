# -*- coding:utf-8 -*-
from django.contrib import admin
from app1.models import Province,City,Yewu
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
    

    
class CityAdmin(admin.ModelAdmin):
    list_display = ('cityname', 'prov','yewu')
    search_fields = ['cityname','provname']
    fieldsets = [  
        ('选择城市', {'fields': ['prov','cityname','yewu']}),  
        ('约束规则', {'fields': ['menu','buss','sms','user']}), 
        ('时间范围', {'fields': ['start','end']}), 
    ]   
#    def change_view(self, request, object_id, extra_context=None):   
#        if request.method == 'POST':
#            return render_to_response('error.html')  
#        return super(CityAdmin, self).change_view(request, object_id,extra_context=None)  
    
admin.site.register(City,CityAdmin)
admin.site.register(Yewu)
admin.site.register(Province)