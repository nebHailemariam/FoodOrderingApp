from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views.common.registration_views import RegisterClient, RegisterDeliveryMan, RegisterRestaurantAdmin
from users.views.common.security_views import login
from users.views.client.profile_views import client_profile
from users.views.deliveryman.profile_views import deliveryman_profile
from users.views.restaurantadmin.profile_views import restaurantadmin_profile
from users.views.restaurantadmin.restaurantadmin_restaurant_views import \
    restaurantadmin_restaurants, restaurantadmin_restaurant, restaurantadmin_restaurant_create,\
    restaurantadmin_menu_create, restaurantadmin_menus, restaurantadmin_menu, restaurantadmin_locations,\
    restaurantadmin_location, restaurantadmin_location_create
from users.views.staff.profile_views import staff_profile
users_router = DefaultRouter()
# users_router.register("route", view)

urlpatterns = [
    url('', include(users_router.urls)),
    # Client Views
    url('register/client/', RegisterClient.as_view()),
    url('client/profile/', client_profile),

    # Deliveryman Views
    url('register/deliveryman/', RegisterDeliveryMan.as_view()),
    url('deliveryman/profile/', deliveryman_profile),

    # Restaurant admin views
    url('register/restaurantadmin/', RegisterRestaurantAdmin.as_view()),
    url('restaurantadmin/profile/', restaurantadmin_profile),
    url('restaurantadmin/restaurant/create/', restaurantadmin_restaurant_create),
    path('restaurantadmin/restaurant/<int:id>/', restaurantadmin_restaurant),
    url('restaurantadmin/restaurants/', restaurantadmin_restaurants),
    path('restaurantadmin/restaurant/<int:restaurant_id>/location/<int:location_id>/menu/create/',
         restaurantadmin_menu_create),
    path('restaurantadmin/restaurant/<int:restaurant_id>/menus/', restaurantadmin_menus),
    path('restaurantadmin/restaurant/menu/<int:menu_id>/', restaurantadmin_menu),
    url('restaurantadmin/restaurant/location/create/', restaurantadmin_location_create),
    path('restaurantadmin/restaurant/<int:restaurant_id>/locations/', restaurantadmin_locations),
    path('restaurantadmin/restaurant/<int:restaurant_id>/locations/<int:location_id>/', restaurantadmin_location),
    path('restaurantadmin/restaurant/menu/create/', restaurantadmin_menu_create),


    # Staff views
    url('staff/profile/', staff_profile),

    # common views
    url('auth-token/login/', login),
]

