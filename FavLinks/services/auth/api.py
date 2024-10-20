from django.contrib.auth import authenticate
from django.db import transaction
from django.contrib.auth.password_validation import validate_password


from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenObtainPairView
from rest_framework.generics import GenericAPIView

from FavLinks.apps.user.models import User
from .serializers import UserRegistrationSerializer, UserSerializer
from ..core import viewsets


class HelloWorld(APIView):
    # permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({
            'message': 'Hello World',
        }, status=status.HTTP_200_OK)
        
class TokenObtainPairView(BaseTokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            username = request.data.get('username')
            password = request.data.get('password')  
            user = authenticate(username=username, password=password)
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RegisterAPIView(GenericAPIView):
    permission_classes = [permissions.AllowAny,]
    @transaction.atomic
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        serializer_data = UserSerializer(user).data
        return Response(serializer_data, status=status.HTTP_201_CREATED)
    

    