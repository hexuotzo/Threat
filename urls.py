from django.conf.urls.defaults import *
from django.conf import settings
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
    (r'^add_city/','Threat.app1.views.city_admin'),
    (r'^add_prov/','Threat.app1.views.prov_admin'),
    (r'^show_city/','Threat.app1.views.jh_city'),
    (r'^show_prov/','Threat.app1.views.jh_prov'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.ADMIN_MEDIA_ROOT}),
)
