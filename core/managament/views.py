from rest_framework import viewsets
from rest_framework.response import Response

from core.managament.models import Product, Inventory
from core.managament.serializers import (
    ProductSerializer,
    ProductCreateSerializer,
    InventorySerializer,
)


class ProductAPIViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreateSerializer

        return ProductSerializer


class InventoryAPIViewSet(viewsets.ModelViewSet):
    
    model = Inventory
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         return InventoryCreateSerializerClass

    #     return InventorySerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = InventoryCreateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         inventory_detail = serializer.save()
            
    #         inventory, created = Inventory.objects.get_or_create(employee=request.user.employee)
    #         if created:
    #             inventory.save()

    #         inventory.products.add(inventory_detail.product)

    #         return Response(InventoryDetailSerializer(inventory_detail).data)
    #     return Response(serializer.errors, status=400)
