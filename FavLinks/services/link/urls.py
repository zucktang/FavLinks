from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    FavoriteURLViewSet,
    TagViewSet,
    CategoryViewSet,

)

router = DefaultRouter()
router.register(r'url', FavoriteURLViewSet)
router.register(r'tag', TagViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]