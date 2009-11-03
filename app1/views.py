# Create your views here.
from models import City,Province
from django.shortcuts import render_to_response

def report(request):
    prov_list = City.objects.filter(provid=111)
    return render_to_response('index.html',locals())

def provlist(request):
    prov_list = Province.objects.all()
    return render_to_response('prov_list.html',locals())

def get_prov(request,tid):
    city_list = City.objects.filter(provid=tid)
    return render_to_response('city_list.html',locals())