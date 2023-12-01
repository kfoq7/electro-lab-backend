from django.urls import path

from core.entities.views import SupplierListCreateAPIView


supplier_list = SupplierListCreateAPIView.as_view()

urlpatterns = [
    path('supplier/', supplier_list, name='supplier-list')
]
