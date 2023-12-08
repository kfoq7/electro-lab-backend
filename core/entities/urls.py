from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.entities.views import (
    SupplierListCreateAPIView,
    EmployeeAPIViewSet,
    StudentAPIViewSet
)


router = DefaultRouter()
router.register('employee', EmployeeAPIViewSet)
router.register('student', StudentAPIViewSet)

supplier_list_create = SupplierListCreateAPIView.as_view()

urlpatterns = [
    path('supplier/', supplier_list_create, name='supplier-list-create'),
    path('', include(router.urls)),
]
