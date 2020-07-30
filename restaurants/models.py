from . import constants
from django.db import models
from users.models import User, Client, DeliveryMan


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ManyToManyField(User, related_name="user_restaurant")
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return self.restaurant.name + ", " + str(self.longitude) + ", " + str(self.latitude)


class Address(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    city = models.TextField(max_length=30)
    sub_city = models.TextField(max_length=30)
    postcode = models.CharField(max_length=5)

    def __str__(self):
        return self.location.restaurant.name + ", " + self.city + ", " + self.sub_city


class Menu(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True, max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    available = models.BooleanField(default=False)
    available_start_date = models.DateTimeField(null=True, blank=True)
    available_end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.restaurant.name + ", " + self.description + ", "


class SubMenu(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    meal_type = models.PositiveSmallIntegerField(choices=constants.MEAL_TYPE_CHOICES)
    description = models.TextField(null=True, max_length=255)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.restaurant.name + ", " + self.description + ", "


class Item(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    submenu = models.ForeignKey(SubMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, max_length=255, blank=True)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.name + ", " + self.restaurant.name


class Order(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    items = models.ManyToManyField(Item, related_name="item_order")
    deliveryman = models.ForeignKey(DeliveryMan, on_delete=models.DO_NOTHING, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=constants.DELIVERY_STATUS_TYPE)
    price = models.IntegerField(null=False)

