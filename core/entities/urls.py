from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.entities.views import EmployeeAPIViewSet


router = DefaultRouter()
router.register(r'employee', EmployeeAPIViewSet, basename='employees')

urlpatterns = router.urls
