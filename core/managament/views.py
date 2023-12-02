from rest_framework import viewsets
from rest_framework.response import Response

from core.managament.models import Product, Inventory
from core.managament.serializers import ProductSerializer, InventorySerializer


class ProductAPIViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InventoryAPIViewSet(viewsets.ModelViewSet):
    
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
