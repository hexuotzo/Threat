from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^threat/', include('threat.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$','threat.views.index'),
    (r'^add_city/','threat.views.city_admin'),
    (r'^add_prov/','threat.views.prov_admin'),
    (r'^logs_city/','threat.views.logs_city'),
    (r'^logs_prov/','threat.views.logs_prov'),
    (r'^logs/','threat.views.show_logs'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.ADMIN_MEDIA_ROOT}),
)
