from rest_framework.routers import DefaultRouter
from users.views import *

router = DefaultRouter()
router.register("clients", ClientViewSet)
router.register("deliverymen", DeliveryManViewSet)
router.register("restaurantadmins", RestaurantAdminViewSet)
router.register("users", UserViewSet)
