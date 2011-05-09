from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'glx.views.home', name='home'),
    # url(r'^glx/', include('glx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^$', 'asset.views.index'),
    
    # asset detail page with comment stream
    (r'^asset/(?P<asset_id>\d+)/$', 'asset.views.detail'),
    
    # add new asset
    (r'^asset/new/', 'asset.views.new'),
    
    # get all assets as kml
    (r'^asset/kml/', 'asset.views.kml'),
    
)
