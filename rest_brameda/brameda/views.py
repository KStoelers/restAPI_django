from brameda.models import *
from brameda.serializers import *
from rest_framework import generics

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRowList(generics.ListCreateAPIView):
    queryset = OrderRow.objects.all()
    serializer_class = OrderRowSerializer

class OrderRowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderRow.objects.all()
    serializer_class = OrderRowSerializer
