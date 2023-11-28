from django.db import models

from ..user.models import User


class Employee(models.Model):
    
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=100, decimal_places=2)
    user = models.OneToOneField(User, related_name='employee', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Supplier(models.Model):
    
    company_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name='supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name
