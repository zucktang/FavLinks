from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction

from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status, exceptions

from FavLinks.apps.link.models import (
    FavoriteURL,
    Category,
    Tag,
)
from FavLinks.services.core import viewsets, mixins

from .serializers import (
    FavoriteURLSerializer,
    CategorySerializer,
    TagSerializer,
)

class FavoriteURLViewSet(mixins.UserViewMixin, viewsets.ModelViewSet):
    queryset = FavoriteURL.objects.all()
    serializer_class = FavoriteURLSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['url', 'category',]
    search_fields = ['url', ]
    ACTION_SERIALIZERS = {
        'list': FavoriteURLSerializer, 
        'retrieve': FavoriteURLSerializer,
        'create': FavoriteURLSerializer,
        'update': FavoriteURLSerializer,
        'partial_update': FavoriteURLSerializer,
        'destroy': FavoriteURLSerializer,
    }
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data
        data.update({"user": request.user.pk})
        serializer = self.get_serializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        serializer = FavoriteURLSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class CategoryViewSet(mixins.UserViewMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ACTION_SERIALIZERS = {
        'list': CategorySerializer, 
        'retrieve': CategorySerializer,
        'create': CategorySerializer,
        'update': CategorySerializer,
        'partial_update': CategorySerializer,
        'destroy': CategorySerializer,
    }
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data
        data.update({"user": request.user.pk})
        serializer = self.get_serializer(data=data, )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        serializer = CategorySerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TagViewSet(mixins.UserViewMixin, viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    ACTION_SERIALIZERS = {
        'list': TagSerializer, 
        'retrieve': TagSerializer,
        'create': TagSerializer,
        'update': TagSerializer,
        'partial_update': TagSerializer,
        'destroy': TagSerializer,
    }

    @transaction.atomic
    def create(self, request, *args, **kwargs):    
        data = request.data
        data.update({"user": request.user.pk})
        serializer = self.get_serializer(data=data, )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        serializer = TagSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    