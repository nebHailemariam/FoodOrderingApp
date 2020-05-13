# users/models.py

from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .managers import UserManager
from . import constants as user_constants
from .constants import *

class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=30, unique=True)
    first_name = models.CharField( max_length=30, blank=True)
    last_name = models.CharField( max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, db_index=True)
    phone = models.CharField(max_length=255,blank=True,null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(choices=user_constants.USER_TYPE_CHOICES)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_client")
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class DeliveryMan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_deliveryman")
    is_verified = models.BooleanField(default=False)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.email


class RestaurantAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_restaurant_admin")
    role = models.PositiveSmallIntegerField(choices=user_constants.RESTAURANT_ADMIN_CHOICES, null=True)

    def __str__(self):
        return self.user.email

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    latitude = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return self.user.username+ ", " + str(self.longitude) + ", " + str(self.latitude)


class Address(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    city = models.TextField(max_length=30)
    sub_city = models.TextField(max_length=30)
    postcode = models.CharField(max_length=5)

    def __str__(self):
        return self.location.user.username + ", " + self.city + ", " + self.sub_city