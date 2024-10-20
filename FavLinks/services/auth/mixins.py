
import jwt
import datetime
from django.conf import settings
from django.http import JsonResponse
from apps.user.models import User
from rest_framework_simplejwt.tokens import RefreshToken

    
class JWTAuthenticationMixin:

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }