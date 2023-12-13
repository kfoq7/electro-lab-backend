from rest_framework import serializers

from core.entities.models import Supplier
from core.managament.models import Product, Inventory, InventoryDetail


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    supplier = SupplierSerializer()

    class Meta:
        model = Product
        fields = '__all__'
        

class InventoryDetailSerializer(serializers.ModelSerializer):

    # product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), read_only=True)
    # iventory = Inve

    class Meta:
        model = InventoryDetail
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):

    products = InventoryDetailSerializer(many=True)

    class Meta:
        model = Inventory
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        products_data = validated_data.pop('products')
        inventory = Inventory.objects.create(**validated_data)
        for product_data in products_data:
            product = product_data.pop('product')
            inventory_detail = InventoryDetail.objects.create(invetory=inventory, product_id=product.id, **product_data)
            inventory.products.add(inventory_detail.product)
        return inventory
