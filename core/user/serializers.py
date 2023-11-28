from rest_framework import serializers
from .models import User


class UserListSeralizer(serializers.ModelSerializer):
    
    profile = serializers.CharField(source='get_profile_display')
    
    class Meta:
        model = User
        fields = '__all__'
