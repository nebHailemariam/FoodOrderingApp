# users/admin.py
from django.contrib import admin
from .models import *


admin.site.register(Client)
admin.site.register(DeliveryMan)
admin.site.register(RestaurantAdmin)
admin.site.register(User)
admin.site.register(Location)
admin.site.register(Address)