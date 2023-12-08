from rest_framework import serializers

from core.entities.models import Supplier
from core.managament.models import Product, Inventory


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    supplier = SupplierSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)

    class Meta:
        model = Inventory
        fields = '__all__'
