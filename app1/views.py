# -*- coding:utf-8 -*-
# Create your views here.
#from models import City,Province
from settings import filter_file
from django.shortcuts import render_to_response
from django import forms
from app1.models import Jihe,Business
import datetime
from django.contrib.admin.views.decorators import staff_member_required

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
def get_date(getstart,getend):
    date_start=getstart.split('-')
    date_end=getend.split('-')
    syear,smonth,sday=int(date_start[0]),int(date_start[1]),int(date_start[2])
    eyear,emonth,eday=int(date_end[0]),int(date_end[1]),int(date_end[2])
    startdate=datetime.date(syear,smonth,sday)
    enddate=datetime.date(eyear,emonth,eday)
    return startdate,enddate

def timecheck(startdate,enddate,cid_list,yewulist):   #验证数据库中同市同业务 是否有时间冲突
	data=Jihe.objects.filter(cid__in=cid_list,yid__in=yewulist)
	for k in data:
		if k.start <= startdate <= k.end or k.start <= enddate <= k.end or (startdate<k.start and enddate>k.end):
		    return False
	return True


class ContactForm(forms.Form):
    sms = forms.BooleanField()
    user = forms.BooleanField()
def show_views(request):
    if request.method == 'POST':
        citylist=request.POST.getlist('cityname')
        provlist=request.POST.getlist('provname')
        if citylist == []:
		    prov_list= Jihe.objects.filter(pid__in=provlist).order_by('-id')
        city_list = Jihe.objects.filter(cid__in=citylist).order_by('-id')
    return render_to_response('jh_list.html',locals())


@staff_member_required
def jh_admin(request):
    business = Business.objects.all()
    form=ContactForm()
    if request.method == 'POST':
        getsms = request.POST.get('sms')
        getuser = request.POST.get('user')
        getstart = request.POST.get('start')
        getend = request.POST.get('end')
        citylist = request.POST.getlist('cityname')
        yewulist = request.POST.getlist('yewuname')
        if getstart=="" or getend=="" or citylist==[] or yewulist==[]:
            result="日期，地市，业务不能为空"
            return render_to_response('myadmin.html',locals())
        days=datetime.timedelta(days=3)      #开始验证时间
        today = datetime.date.today()		
        startdate,enddate=get_date(getstart,getend)
        if startdate >= enddate:
            result= "开始日期必须早于结束日期"
            return render_to_response('myadmin.html',locals())
        if startdate - days <= today:
            result= "不能设置3天之内的规则"
            return render_to_response('myadmin.html',locals())
        cid_list=map(lambda x:x[4:7],citylist)	#取市ID
        if not timecheck(startdate,enddate,cid_list,yewulist):
            result="选中的城市与业务，与已存在的规则有冲突"
            return render_to_response('myadmin.html',locals())
        num1,num2=0,0
        qz1,qz2="no","no"		
        if getsms=="on":
            num1=2
            qz1="yes"
        if getuser=="on":
            num2=4
            qz2="yes"
        quanzhi=num1+num2
#存数据,写log
        f=open(filter_file,"a")
        for i in citylist:   
            i=i.split('_')
            provid,cityid,cname=i[0],i[1],i[2]
            for j in yewulist:
                yw = Business.objects.filter(yid=j)[0]
                jihe = Jihe(city=cname,cid=cityid,prov=provinces[provid],pid=provid,yid=j,yewu=yw.yname,sms=qz1,user=qz2,start=startdate,end=enddate,qz=quanzhi)
                jihe.save()
                msg="%s|%s|%s|%s|%s|%s\n"%(startdate,enddate,provid,cityid,j,quanzhi)
                f.write(msg)
        f.close()    
        result="------添加成功------"
    return render_to_response('myadmin.html',locals())

