from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import Group


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):

        if not username:
            raise ValueError('The username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        if len(self.model.objects.filter(username=user.username)) == 0:
            raise Exception("Internal error")
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault("groups_id", Group.objects.filter(name="Superuser").first().pk)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)