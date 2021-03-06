from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.cartRemove, name="CartRemove"),
    url(r'^add/(?P<product_id>\d+)/$', views.cartAdd, name="CartAdd"),
    url(r'ajaxadd/(?P<product_id>\d+)/$', views.ajaxcartAdd, name="AjaxCartAdd"),
    url(r'^$', views.cartDetail, name="CartDetail"),
]
