from django.urls import path

from rest_framework.routers import DefaultRouter

from core.managament.views import ProductAPIViewSet


router = DefaultRouter()
router.register(r'product', ProductAPIViewSet)

urlpatterns = router.urls
