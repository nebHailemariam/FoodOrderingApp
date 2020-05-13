from django.contrib import admin
from .models import *

admin.site.register(Restaurant)
admin.site.register(Address)
admin.site.register(Location)
admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(Item)

