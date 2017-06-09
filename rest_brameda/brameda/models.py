from django.db import models

class Customer(models.model):
	first_name = models.Charfield(max_length=50)
	last_name = models.Charfield(max_length=50)
	email = models.Charfield(max_length=50)
	address = models.Charfield(max_length=50)
	
class Product(models.model):
	name = models.Charfield(max_length=75)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	product_id = models.IntegerField()

class Order(models.model):
	order_id = models.IntegerField()
	order_rows = models.IntegerField()
	
class OrderRow(models.model):
	order_row_id = models.IntegerField()
	product = models.IntegerField()
	amount = models.IntegerField()

	
	
	
	
