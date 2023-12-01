from rest_framework import serializers

from core.user.models import User
from core.entities.models import Employee, Supplier


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    
    class Meta:
        model = Employee
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'
