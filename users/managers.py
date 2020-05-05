# users/managers.py
from django.contrib.auth.models import BaseUserManager
from . import constants as user_constants
from .models import *

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        print(user.__dict__)
        user.save()
        if len(User.objects.filter(email=user.email)) == 0:
            raise Exception("Internal error")
        return

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('user_type', user_constants.SUPERUSER)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
