from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from users.views.common.registration_views import RegisterClient, RegisterDeliveryMan, RegisterRestaurantAdmin
from users.views.common.security_views import LoginView
from users.views.client.profile_views import client_profile
from users.views.deliveryman.profile_views import deliveryman_profile
from users.views.restaurantadmin.profile_views import restaurantadmin_profile
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

    # Stuff views
    url('staff/profile/', staff_profile),

    # common views
    url('auth-token/login/', LoginView.as_view()),
]
