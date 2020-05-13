from django.db import models
from . import constants


class Restaurant(models.Model):
    name = models.CharField(primary_key=True, max_length=30, unique=True)
    description = models.TextField(null=True, max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    latitude = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return self.restaurant.name + ", " + str(self.longitude) + ", " + str(self.latitude)


class Address(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    city = models.TextField(max_length=30)
    sub_city = models.TextField(max_length=30)
    postcode = models.CharField(max_length=5)

    def __str__(self):
        return self.location.restaurant.name + ", " + self.city + ", " + self.sub_city


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.TextField(null=True, max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    available = models.BooleanField(default=False)
    available_start_date = models.DateTimeField()
    available_end_date = models.DateTimeField()

    def __str__(self):
        return self.restaurant.name + ", " + self.description + ", "


class SubMenu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ManyToManyField(Menu)
    meal_type = models.PositiveSmallIntegerField(choices=constants.MEAL_TYPE_CHOICES)
    description = models.TextField(null=True, max_length=255)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.restaurant.name + ", " + self.description + ", "


class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    submenu = models.ManyToManyField(SubMenu)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, max_length=255, blank=True)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.name + ", " + self.restaurant.name

