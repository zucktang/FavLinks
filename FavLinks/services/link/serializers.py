from django.db import transaction

from rest_framework import serializers

from FavLinks.apps.link.models import (
    FavoriteURL,
    Category,
    Tag,
)

        
class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('id', 'name')
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        

class FavoriteURLSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    tags = TagSerializer(many=True, required=False)
    class Meta:
        model = FavoriteURL
        fields = '__all__'
        
    @transaction.atomic    
    def create(self, validated_data):
        user = self.context['request'].user
        category_data = validated_data.pop('category', None)
        if category_data:
            category, created = Category.objects.get_or_create(user=user, **category_data)
            validated_data['category'] = category
        
        tags_data = validated_data.pop('tags', [])
        tags = []
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(user=user, **tag_data)
            tags.append(tag)
        
        instance = FavoriteURL.objects.create(**validated_data)
        instance.tags.set(tags) 
        
        return instance
        
    
    
