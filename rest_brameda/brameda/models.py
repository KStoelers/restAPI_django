from django.db import models

class Customer(models.Model):
	customer_id = models.CharField(max_length=50, unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	
class Product(models.Model):
	product_id = models.CharField(max_length=50, unique=True)
	name = models.CharField(max_length=75)
	price = models.DecimalField(max_digits=5, decimal_places=2)

class Order(models.Model):
	order_id = models.CharField(max_length=50, unique=True)
	order_rows = models.IntegerField()
	
class OrderRow(models.Model):
	order_row_id = models.CharField(max_length=50, unique=True)
	product = models.IntegerField()
	amount = models.IntegerField()

	
	
	
	
