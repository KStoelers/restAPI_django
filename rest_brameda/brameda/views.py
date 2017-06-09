from brameda.models import *
from django.http import Http404

from brameda.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CustomerList(APIView):
    """ List all customers """
def get(self, request, format=None):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

class CustomerDetail(APIView):
    """ Create, retrieve, update or delete a customer instance"""
def post(self, request, format=None):
    serializer = CustomerSerializer(data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
def get_object(self, pk):
    try:
        return Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        raise Http404

def get(self, request, pk, format=None):
    customer = self.get_object(pk)
    customer = CustomerSerializer(customer)
    return Response(customer.data)

def put(self, request, pk, format=None):
    customer = self.get_object(pk)
    serializer = CustomerSerializer(customer, data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self, request, pk, format=None):
    customer = self.get_object(pk)
    customer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(APIView):
    """ List all products """
def get(self, request, format=None):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

class ProductDetail(APIView):
    """ retrieve a product instance"""		
def get_object(self, pk):
    try:
        return Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
			
class OrderList(APIView):
    """ List all orders """
def get(self, request, format=None):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

class OrderDetail(APIView):
    """ Create, retrieve, update or delete an order instance"""
def post(self, request, format=None):
    serializer = OrderSerializer(data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
def get_object(self, pk):
    try:
        return Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        raise Http404

def get(self, request, pk, format=None):
    order = self.get_object(pk)
    order = OrderSerializer(order)
    return Response(order.data)

def put(self, request, pk, format=None):
    order = self.get_object(pk)
    serializer = OrderSerializer(order, data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self, request, pk, format=None):
    order = self.get_object(pk)
    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class OrderRowList(APIView):
    """ List all orderrows """
def get(self, request, format=None):
    orderrows = OrderRow.objects.all()
    serializer = OrderRowSerializer(orderrows, many=True)
    return Response(serializer.data)

class OrderRowDetail(APIView):
    """ Create, retrieve, update or delete an orderrow instance"""
def post(self, request, format=None):
    serializer = OrderRowSerializer(data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
def get_object(self, pk):
    try:
        return OrderRow.objects.get(pk=pk)
    except OrderRow.DoesNotExist:
        raise Http404

def get(self, request, pk, format=None):
    orderrow = self.get_object(pk)
    orderrow = OrderRowSerializer(orderrow)
    return Response(orderrow.data)

def put(self, request, pk, format=None):
    orderrow = self.get_object(pk)
    serializer = OrderRowSerializer(orderrow, data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self, request, pk, format=None):
    orderrow = self.get_object(pk)
    orderrow.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)