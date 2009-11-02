# Create your views here.
from models import City
from django.shortcuts import render_to_response

def report(request):
    prov_list = City.objects.filter(provid=111)
    return render_to_response('index.html',locals())