# -*- coding:utf-8 -*-
from django.contrib import admin
from app1.models import Province,City,Yewu

class CityAdmin(admin.ModelAdmin):
#    #date_hierarchy = 'date'
    list_display = ('cityname', 'prov','yewu')
#    list_display_links = ('msg',)
#    #list_editable = ('msg',)
#    list_filter = ('name',)
#    #list_per_page = 5
#    #prepopulated_fields = {"msg": ("hour",)}
    search_fields = ['cityname']
    fieldsets = [  
        ('选择城市', {'fields': ['prov','cityname','yewu']}),  
        ('约束规则', {'fields': ['menu','buss','sms','user']}), 
        ('时间范围', {'fields': ['start','end']}), 
    ]
    
admin.site.register(Yewu)
admin.site.register(Province)
admin.site.register(City,CityAdmin)