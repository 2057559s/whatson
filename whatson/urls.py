from django.conf.urls import patterns, url
from whatson import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^home/', views.home, name='home'),
        url(r'^register/', views.register, name='register'),
        url(r'^login/', views.user_login, name='login'),
        url(r'^logout/', views.user_logout, name='logout'),
        url(r'^settings/', views.settings, name='settings'),
        url(r'^about/', views.about, name='about'),
        url(r'^new_calendar/', views.new_calendar, name='new_calendar'),

)