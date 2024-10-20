from .abstract_models import (
    AbstractFavoriteURL,
    AbstractCategory,
    AbstractTag,
)
from django.db import models



class FavoriteURL(AbstractFavoriteURL):
    user = models.ForeignKey(
        'user.User', 
        on_delete=models.CASCADE
    )
    
    class Meta:
        unique_together = ('user', 'url')


class Category(AbstractCategory):
    user = models.ForeignKey(
        'user.User', 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    class Meta:
        unique_together = ('user', 'name')


class Tag(AbstractTag):
    user = models.ForeignKey(
        'user.User', 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    class Meta:
        unique_together = ('user', 'name')
