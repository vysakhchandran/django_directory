from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib import admin
from . import views
app_name = 'app1'

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^add/', views.Directory_Add, name='add'),
    url(r'^(?P<slug>[-\w]+)/edit', views.Directory_Detail, name='edit'),
    url(r'^search/$', views.submit_search, name='number_search'),
    url(r'^api/get_names/', views.get_names, name='get_names'),



]