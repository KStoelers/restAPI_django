from brameda.models import *

from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email', 'address')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('product_id', 'name', 'price')

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('order_id', 'order_rows')
		
class OrderRowSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderRow
		fields = ('order_row_id', 'product', 'amount')