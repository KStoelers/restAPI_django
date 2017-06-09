from django.conf.urls import patterns, url

from brameda import views

customer_urls = patterns('',
  url(r'^edit/(?P<pk>\d+)$', views.CustomerUpdate.as_view(), name='customer_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.CustomerDelete.as_view(), name='customer_delete'),
)

product_urls = patterns('',
  url(r'^edit/(?P<pk>\d+)$', views.ProductUpdate.as_view(), name='product_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.ProductDelete.as_view(), name='product_delete'),
)

order_urls = patterns('', 
  url(r'^edit/(?P<pk>\d+)$', views.OrderUpdate.as_view(), name='order_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.OrderDelete.as_view(), name='order_delete'),
)

orderrow_urls = patterns('',
  url(r'^edit/(?P<pk>\d+)$', views.OrderRowUpdate.as_view(), name='orderrow_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.OrderRowDelete.as_view(), name='orderrow_delete'),
)

urlpatterns = patterns('',
  url(r'^$', views.CustomerList.as_view(), name='customer_list'),
  url(r'^new$', views.CustomerCreate.as_view(), name='customer_new'),
  url(r'^$', views.ProductList.as_view(), name='product_list'),
  url(r'^new$', views.ProductCreate.as_view(), name='product_new'),
  url(r'^$', views.OrderList.as_view(), name='order_list'),
  url(r'^new$', views.OrderCreate.as_view(), name='order_new'),
  url(r'^$', views.OrderRowList.as_view(), name='orderrow_list'),
  url(r'^new$', views.OrderRowCreate.as_view(), name='orderrow_new'),
)