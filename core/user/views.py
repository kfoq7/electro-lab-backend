from rest_framework import viewsets
from .models import User
from .serializers import UserListSeralizer


class UserListAPIView(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserListSeralizer
