from rest_framework import serializers

from core.user.models import User
from core.entities.models import Employee, Supplier, Student
from core.managament.serializers import ProductSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(validated_data):
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
        employee = Employee.objects.create(user=user, **validated_data)
        return employee


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'code_student', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance = User.objects.create(**user_data)

        student_instance = Student.objects.create(user=user_instance, **validated_data)
        return student_instance
