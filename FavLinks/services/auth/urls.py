from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .api import TokenObtainPairView, RegisterAPIView
from .api import HelloWorld

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorld.as_view(), name='hello_world'),
]