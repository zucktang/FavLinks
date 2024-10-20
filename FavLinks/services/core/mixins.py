
from rest_framework import exceptions
from django.contrib.auth import get_user_model

class ActionSerializersViewSetMixin:

    ACTION_SERIALIZERS = {}

    def get_serializer_class(self):
        return self.ACTION_SERIALIZERS.get(self.action, self.serializer_class)
    
class UserViewMixin():
    
    def get_user(self):
        user = self.request.user
        if isinstance(user, get_user_model()):
            return user
        else:
            raise exceptions.APIException('This section for customer only.')
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.get_user()
        return queryset.filter(user=user)
