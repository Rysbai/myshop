from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^process/$', views.paymentProcess, name='process'),
    url(r'^done/$', views.paymentDone, name='done'),
    url(r'canceled/$', views.panymentCanceled, name='canceled'),
]
