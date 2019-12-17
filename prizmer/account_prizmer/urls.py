# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prizmer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.account),
    url(r'^electric_info', views.electric_info),
    url(r'^heat_info', views.heat_info),
    url(r'^water_info', views.water_info),
    url(r'^exit', views.go_out),

)
