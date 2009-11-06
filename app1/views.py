# Create your views here.
from models import City,Province
from django.shortcuts import render_to_response

def get_prov(request):
    if request.method == 'POST':
        citylist=request.POST.getlist('cityname')
        provlist=request.POST.getlist('provname')
        if citylist == []:
            prov_list= City.objects.filter(provid__in=provlist).order_by('-id')
        city_list = City.objects.filter(citynum__in=citylist).order_by('-id')
    return render_to_response('city_list.html',locals())
