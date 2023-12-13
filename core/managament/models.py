import datetime

from django.db import models

from core.entities.models import Employee, Supplier


class Product(models.Model):
    
    name_product = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    unique_stock = models.BigIntegerField()
    

class Inventory(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='inventory_products', through='InventoryDetail')
    delivery_day = models.DateField(default=datetime.date.today)
    total_products = models.BigIntegerField(default=0)


class InventoryDetail(models.Model):

    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, null=True, blank=True)
