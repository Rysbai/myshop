from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'login/$', views.login, name='login'),
    url(r'logout/$', views.logout, name='logout'),
    url(r'register/$', views.register, name='register'),
    url(r'password_change/$', views.password_change, name='password_change'),
    url(r'password_change_done/$', views.password_change_done, name='password_change_done'),
    url(r'personal_area/$', views.personal_area, name='personal_area'),
]
