from rest_framework import serializers

from core.user.models import User
from core.entities.models import Employee, Supplier


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        return user


class EmployeeSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(user_data)
        supplier = Supplier.objects.create(user=user, **validated_data)
        return supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'
