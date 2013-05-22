from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from core import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'job.views.home', name='home'),
    # url(r'^job/', include('job.foo.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^ajax-type/', views.ajax_type, name='ajax_type'),
    url(r'^ajax-vacancy/', views.ajax_vacancy, name='ajax_vacancy'),
    url(r'^ajax-search/', views.ajax_search, name='ajax_search'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
