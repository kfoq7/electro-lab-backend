from rest_framework import viewsets
from lab_user.models import UserCustom
from lab_user.serializers import UserListSeralizer


class UserListAPIView(viewsets.ModelViewSet):
    
    queryset = UserCustom.objects.all()
    serializer_class = UserListSeralizer
