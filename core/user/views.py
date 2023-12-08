from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

from user.models import User
from user.serializers import UserListSeralizer


class UserListAPIView(viewsets.ModelViewSet):

    model = User
    queryset = User.objects.all()
    serializer_class = UserListSeralizer


class Login(ObtainAuthToken):
    
    def post(self, request, *args, kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if not login_serializer.is_valid():
            return Response({
            'error': 'username or password wrong'
        }, status = status.HTTP_400_BAD_REQUEST)

        user = login_serializer.validated_data['user']
        # token, _ = Token.objects.get_or_create(user=user)
        if not user.isActive:
            return Response({
                'msg': 'User is not active'
            }, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            # 'token': token.key,
            'user': self.get_data_usuario(user),
            'msg':'inicio de sesión exitoso.'
        }, status = status.HTTP_200_OK)
