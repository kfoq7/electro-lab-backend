from django.db import models

from core.entities.models import Employee, Supplier


class Product(models.Model):
    
    name_product = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    unique_stock = models.BigIntegerField()
    

class Inventory(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products', through='InventoryDetail')


class InventoryDetail(models.Model):
    
    invetory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_day = models.DateField()
    total_products = models.BigIntegerField()
    description = models.TextField(max_length=255, null=True, blank=True)
