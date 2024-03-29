from django.db import models

from core.user.models import User


class Employee(models.Model):

    salary = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.OneToOneField(User, related_name='employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Supplier(models.Model):

    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Student(models.Model):

    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    code_student = models.IntegerField()
    products = models.ManyToManyField('managament.Product', related_name='studens_products')

    def __str__(self):
        return self.user.name
