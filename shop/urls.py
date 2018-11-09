from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.productList, name="ProductListByCategory"),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.productDetail, name="ProductDetail"),
    url(r'^$', views.productList, name="ProductList"),
]
