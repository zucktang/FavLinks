from .abstract_models import AbstractUser
from django.contrib.auth.models import AbstractUser as BaseAbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(BaseAbstractUser, AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
        