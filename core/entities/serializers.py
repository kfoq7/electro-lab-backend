from rest_framework import serializers

from core.user.models import User
from entities.models import Employee


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    
    class Meta:
        model = Employee
        fields = '__all__'
