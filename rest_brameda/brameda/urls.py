from django.conf.urls import *
from brameda import views

urlpatterns = [
    url(r'^customers/', views.CustomerList.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    url(r'^products/', views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^orders/', views.OrderList.as_view(), name='order_list'),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
    url(r'^orderrows/', views.OrderRowList.as_view(), name='orderrow_list'),
    url(r'^orderrows/(?P<pk>[0-9]+)/$', views.OrderRowDetail.as_view()),
]