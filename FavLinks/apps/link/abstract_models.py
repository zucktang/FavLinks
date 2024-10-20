import uuid
from django.db import models
from ..core.models import BaseModel

class AbstractFavoriteURL(BaseModel):
    url = models.URLField()
    title = models.CharField(
        max_length=255,
        default='Untitled'
    )
    category = models.ForeignKey(
        'link.Category', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        default=None
    )
    tags = models.ManyToManyField(
        'link.Tag', 
        blank=True,
        default=None
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        abstract = True
        

class AbstractCategory(models.Model):
    name = models.CharField(max_length=255, )
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True
        

class AbstractTag(models.Model):
    name = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True
    
