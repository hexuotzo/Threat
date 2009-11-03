from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^Threat/', include('Threat.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^report/','Threat.app1.views.report'),
    (r'^province/', 'Threat.app1.views.provlist'),
    (r'^prov/(?P<tid>.*)/','Threat.app1.views.get_prov')
    #(r'^city/(?P<tid>.*)/', 'Threat.app1.views.get_city'),
)
