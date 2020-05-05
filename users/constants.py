from django.db import models

SUPERUSER = 1
STAFF = 2
DELIVERYMAN= 3
RESTAURANT_ADMIN = 4
CLIENT = 5

USER_TYPE_CHOICES = (
      (SUPERUSER, 'Superuser'),
      (STAFF, 'Staff'),
      (DELIVERYMAN, 'Deliveryman'),
      (RESTAURANT_ADMIN, 'Restaurant admin'),
      (CLIENT, 'Client'),
)

SUPER_RESTAURANT_ADMIN = 1
SUB_RESTAURANT_ADMIN = 2

RESTAURANT_ADMIN_CHOICES = (
    (SUPER_RESTAURANT_ADMIN, "Super restaurant admin"),
    (SUB_RESTAURANT_ADMIN, "Sub restaurant admin")
)
