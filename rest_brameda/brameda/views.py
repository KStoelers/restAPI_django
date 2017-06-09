from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from brameda.models import Customer, Product, Order, OrderRow

class CustomerList(ListView):
	model = Customer
	
class CustomerCreate(CreateView):
	model = Customer
	success_url = reverse('customer_list')
	fields = ['first_name', 'last_name', 'email', 'address']

class CustomerUpdate(UpdateView):
	model = Customer
	success_url = reverse('customer_list')
	fields = ['first_name', 'last_name', 'email', 'address']

class CustomerDelete(DeleteView):
	model = Customer
	success_url = reverse('customer=_list')
	
class ProductList(ListView):
	model = Product
	
class ProductCreate(CreateView):
	model = Product
	success_url = reverse('product_list')
	fields = ['name', 'price', 'product_id']

class ProductUpdate(UpdateView):
	model = Product
	success_url = reverse('product_list')
	fields = ['name', 'price', 'product_id']

class ProductDelete(DeleteView):
	model = Product
	success_url = reverse('product_list')
	
class OrderList(ListView):
	model = Order
	
class OrderCreate(CreateView):
	model = Order
	success_url = reverse('order_list')
	fields = ['order_id', 'order_rows']

class OrderUpdate(UpdateView):
	model = Order
	success_url = reverse('order_list')
	fields = ['order_id', 'order_rows']

class OrderDelete(DeleteView):
	model = Order
	success_url = reverse('order_list')

class OrderRowList(ListView):
	model = OrderRow
	
class OrderRowCreate(CreateView):
	model = OrderRow
	success_url = reverse('orderrow_list')
	fields = ['order_row_id', 'product', 'amount']

class OrderRowUpdate(UpdateView):
	model = OrderRow
	success_url = reverse('orderrow_list')
	fields = ['order_row_id', 'product', 'amount']

class OrderRowDelete(DeleteView):
	model = OrderRow
	success_url = reverse('orderrow_list')
	
