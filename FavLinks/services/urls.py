from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path(r'auth/', include('FavLinks.services.auth.urls')),
    path(r'favorite/link/', include('FavLinks.services.link.urls')),
]