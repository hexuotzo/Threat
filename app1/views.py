# Create your views here.
from models import City,Province
from django.conf.urls.defaults import *
from django.shortcuts import render_to_response

def report(request):
    prov_list = City.objects.order_by('id')
    return render_to_response('index.html',locals())
