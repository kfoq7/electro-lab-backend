from django.urls import path

from rest_framework.routers import DefaultRouter

from core.managament.views import ProductAPIViewSet, InventoryAPIViewSet


router = DefaultRouter()
router.register('product', ProductAPIViewSet)
router.register('inventory',InventoryAPIViewSet)

urlpatterns = router.urls
