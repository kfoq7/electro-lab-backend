from rest_framework import status, viewsets, generics
from rest_framework.response import Response

from core.entities.models import Employee, Supplier
from core.entities.serializers import EmployeeSerializer, SupplierSerializer


class EmployeeAPIViewSet(viewsets.ModelViewSet):

    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def create(self, request, pk=None, *args, **kwargs):
        employee_serializer = self.get_serializer(data=request.data)
        if not employee_serializer.is_valid():
            return Response({
                'msg': employee_serializer.error
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'msg': 'Employee created successfully',
            'data': employee_serializer.data
        }, status=status.HTTP_201_CREATED)


class SupplierListCreateAPIView(generics.ListCreateAPIView):

    model = Supplier
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
