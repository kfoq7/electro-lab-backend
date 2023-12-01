from rest_framework import viewsets
from rest_framework.response import Response

from core.managament.models import Product
from core.managament.serializers import ProductSerializer


class ProductAPIViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
