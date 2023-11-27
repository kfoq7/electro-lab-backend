from rest_framework import serializers
from lab_user.models import UserCustom


class UserListSeralizer(serializers.ModelSerializer):
    
    profile = serializers.CharField(source='get_profile_display')
    
    class Meta:
        model = UserCustom
        fields = '__all__'
