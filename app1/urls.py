from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib import admin
from . import views
app_name = 'app1'

urlpatterns = [
	url(r'^$', views.IndexView, name='index'),
    url(r'^login/', views.login, name='login'),

    url(r'^add/', views.Directory_Add, name='add'),
    url(r'^(?P<slug>[-\w]+)/edit', views.Directory_Detail, name='edit'),
    url(r'^home/', views.IndexView, name='index'),
    url(r'^logout/', views.logout,name='logout'),

]