# -*- coding:utf-8 -*-
# Create your views here.
#from models import City,Province
from django.shortcuts import render_to_response
from django import forms
from app1.models import Jihe
import datetime

provinces = {
	'100':'北京市',
	'200':'广东省',
	'210':'上海市',
	'220':'天津市',
	'230':'重庆市',
	'240':'辽宁省',
	'250':'江苏省',
	'270':'湖北省',
	'280':'四川省',
	'290':'陕西省',
	'311':'河北省',
	'351':'山西省',
	'371':'河南省',
	'431':'吉林省',
	'451':'黑龙江省',
	'471':'内蒙古自治区',
	'531':'山东省',
	'551':'安徽省',
	'571':'浙江省',
	'591':'福建省',
	'731':'湖南省',
	'771':'广西壮族自治区',
	'791':'江西省',
	'851':'贵州省',
	'871':'云南省',
	'891':'西藏自治区',
	'898':'海南省',
	'931':'甘肃省',
	'951':'宁夏回族自治区',
	'971':'青海省',
	'991':'新疆维吾尔自治区',
}

def get_prov(request):
    if request.method == 'POST':
        citylist=request.POST.getlist('cityname')
        provlist=request.POST.getlist('provname')
        if citylist == []:
            prov_list= Jihe.objects.filter(pid__in=provlist).order_by('-id')
        city_list = Jihe.objects.filter(cid__in=citylist).order_by('-id')
    return render_to_response('city_list.html',locals())
 

def timecheck(start,end,citylist,yewulist):
    if start=="" or end=="" or citylist==[] or yewulist==[]:
        return False
    days=datetime.timedelta(days=3)
    today = datetime.date.today()
    date_start=start.split('-')
    date_end=end.split('-')
    syear,smonth,sday=int(date_start[0]),int(date_start[1]),int(date_start[2])
    eyear,emonth,eday=int(date_end[0]),int(date_end[1]),int(date_end[2])
    startdate=datetime.date(syear,smonth,sday)
    enddate=datetime.date(eyear,emonth,eday) #生成开始与结束日期，用于与数据库信息比对
    for i in citylist:
        i=i.split('_')
        provid,cityid,cname=i[0],i[1],i[2]
        for j in yewulist:
            data=Jihe.objects.filter(cid=cityid,yewu=j)
            for k in data:
                print "1111111111111111"
                if startdate >= enddate:
                    return False
                elif startdate - days <= today:
                    return False
                for j in data:
                    print "2222222222222"
                    if j.start <= startdate <= j.end or j.start <= enddate <= j.end or (startdate<j.start and enddate>j.end):
                        return False
    
    return True

class ContactForm(forms.Form):
    sms = forms.BooleanField()
    user = forms.BooleanField() 
     
def jh_admin(request):
    form=ContactForm()
    if request.method == 'POST':
        num1,num2=0,0
        qz1,qz2="no","no"
        getsms = request.POST.get('sms')
        getuser = request.POST.get('user')
        getstart = request.POST.get('start')
        getend = request.POST.get('end')
        citylist = request.POST.getlist('cityname')
        yewulist = request.POST.getlist('yewuname')
        if getsms=="on":
            num1=2
            qz1="yes"
        if getuser=="on":
            num2=4
            qz2="yes"
        if timecheck(getstart,getend,citylist,yewulist):
            for i in citylist:
                i=i.split('_')
                provid,cityid,cname=i[0],i[1],i[2]
                for j in yewulist:
                    quanzhi=num1+num2
                    date_start=getstart.split('-')
                    date_end=getend.split('-')
                    syear,smonth,sday=int(date_start[0]),int(date_start[1]),int(date_start[2])
                    eyear,emonth,eday=int(date_end[0]),int(date_end[1]),int(date_end[2])
                    startdate=datetime.date(syear,smonth,sday)
                    enddate=datetime.date(eyear,emonth,eday) 
                    jihe = Jihe(city=cname,cid=cityid,prov=provinces[provid],pid=provid,yewu=j,sms=qz1,user=qz2,start=startdate,end=enddate,qz=quanzhi)
                    jihe.save()
                    f=open("target/filter_config","a")
                    msg="%s|%s|%s|%s|%s|%s\n"%(startdate,enddate,provid,cityid,j,quanzhi)
                    f.write(msg)
                    f.close() #写LOG                    
            result="------添加成功------"
            return render_to_response('myadmin.html',locals())
        result="!!------error------!!"
    form=ContactForm()
    return render_to_response('myadmin.html',locals())