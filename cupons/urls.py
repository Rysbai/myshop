from django.conf.urls import url
from cupons import views

urlpatterns = [
    url(r'^apply', views.cuponApply, name='apply'),
]
