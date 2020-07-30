from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views.common.registration_views import RegisterClient, RegisterDeliveryMan, RegisterRestaurantAdmin
from users.views.common.security_views import login
from users.views.client.profile_views import client_profile
from users.views.client.order_views import client_list_restaurants, client_list_restaurant, client_list_restaurant_menus, \
    client_list_restaurant_menu, client_list_restaurant_submenu, client_order
from users.views.deliveryman.profile_views import deliveryman_profile
from users.views.restaurantadmin.profile_views import restaurantadmin_profile
from users.views.restaurantadmin.restaurantadmin_restaurant_views import \
    restaurantadmin_restaurants, restaurantadmin_restaurant, restaurantadmin_restaurant_create,\
    restaurantadmin_menu_create, restaurantadmin_menus, restaurantadmin_menu, restaurantadmin_locations,\
    restaurantadmin_location, restaurantadmin_location_create, restaurantadmin_submenu_create, restaurantadmin_submenus,\
    restaurantadmin_item_create, restaurantadmin_item
from users.views.staff.profile_views import staff_profile
users_router = DefaultRouter()
# users_router.register("route", view)

urlpatterns = [
    url('', include(users_router.urls)),
    # Client Views
    url('client/register/', RegisterClient.as_view()),
    url('client/profile/', client_profile),
    url('client/restaurants/', client_list_restaurants),
    path('client/restaurant/<int:restaurant_id>/', client_list_restaurant),
    path('client/restaurant/<int:restaurant_id>/menus/', client_list_restaurant_menus),
    path('client/restaurant/menu/<int:menu>/', client_list_restaurant_menu),
    path('client/restaurant/submenu/<int:submenu>/', client_list_restaurant_submenu),
    path('client/restaurant/order/', client_order),

    # Deliveryman Views
    url('deliveryman/register/', RegisterDeliveryMan.as_view()),
    url('deliveryman/profile/', deliveryman_profile),

    # Restaurant admin views
    url('restaurantadmin/register/', RegisterRestaurantAdmin.as_view()),
    url('restaurantadmin/profile/', restaurantadmin_profile),
    url('restaurantadmin/restaurant/create/', restaurantadmin_restaurant_create),
    path('restaurantadmin/restaurant/<int:id>/', restaurantadmin_restaurant),
    url('restaurantadmin/restaurants/', restaurantadmin_restaurants),
    path('restaurantadmin/restaurant/<int:restaurant_id>/menu/', restaurantadmin_menus),
    path('restaurantadmin/restaurant/menu/<int:menu_id>/', restaurantadmin_menu),
    url('restaurantadmin/restaurant/location/create/', restaurantadmin_location_create),
    path('restaurantadmin/restaurant/<int:restaurant_id>/locations/', restaurantadmin_locations),
    path('restaurantadmin/restaurant/<int:restaurant_id>/locations/<int:location_id>/', restaurantadmin_location),
    url('restaurantadmin/restaurant/menu/create/', restaurantadmin_menu_create),
    url('restaurantadmin/restaurant/menu/submenu/create/', restaurantadmin_submenu_create),
    path('restaurantadmin/restaurant/<int:restaurant_id>/menu/<int:menu_id>/submenus/', restaurantadmin_submenus),
    url('restaurantadmin/restaurant/item/create/', restaurantadmin_item_create),
    path('restaurantadmin/restaurant/item/', restaurantadmin_item_create),
    path('restaurantadmin/restaurant/item/<int:id>/', restaurantadmin_item),
    # Staff views
    url('staff/profile/', staff_profile),

    # common views
    url('auth-token/login/', login),
]

