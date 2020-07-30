import django
import os,sys


sys.path.append("..")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeliveryApp.settings')
django.setup()
from django.contrib.auth.models import Group

GROUPS= ['Superuser','Staff', 'Deliveryman', 'Restaurant admin','Client']
MODELS = ['user']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
