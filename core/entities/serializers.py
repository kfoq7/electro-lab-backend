from rest_framework import serializers

from core.user.models import User
from core.entities.models import Employee


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


class EmployeeSerializer(UserSerializer, serializers.ModelSerializer):
    
    user = UserSerializer()
    
    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        # user = self.fields['user']
        # print(user)
        pass
