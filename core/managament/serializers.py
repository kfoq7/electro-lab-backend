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
        fields = ('id', 'name_product', 'unique_stock', 'supplier', )


class ProductCreateSerializer(serializers.ModelSerializer):

    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all()) 

    class Meta:
        model = Product
        fields = ('name_product', 'unique_stock', 'supplier', )


class InventoryDetailSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.IntegerField(source='product.id')
    name_product =  serializers.ReadOnlyField(source='product.name_product')
    description = serializers.ReadOnlyField()

    class Meta:
        model = InventoryDetail
        fields = ('id', 'name_product', 'description')


class InventoryCreateSerializer(serializers.ModelSerializer):
    
    products = InventoryDetailSerializer(many=True)
    
    class Meta:
        model = Inventory
        fields = '__all__'

    def create(self, validated_data):
        products = validated_data.pop('products', [])
        inventory = Inventory.objects.create(**validated_data)

        for product_data in products:
            _, product = product_data.popitem()
            product_id = product.get('id')
            inventory_detail = InventoryDetail.objects.create(inventory=inventory, product_id=product_id)
            inventory.products.add(inventory_detail.product)

        return inventory


class InventorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)

    class Meta:
        model = Inventory
        fields = '__all__'
