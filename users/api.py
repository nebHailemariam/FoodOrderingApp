from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from users.views.common.registration_views import RegisterClient, RegisterDeliveryMan, RegisterRestaurantAdmin
from users.views.common.security_views import LoginView
users_router = DefaultRouter()
# users_router.register("route", view)


urlpatterns = [
    url('', include(users_router.urls)),
    url('register/client/', RegisterClient.as_view()),
    url('register/deliveryman/', RegisterDeliveryMan.as_view()),
    url('register/restaurantadmin/', RegisterRestaurantAdmin.as_view()),
    url('auth-token/login/', LoginView.as_view()),
]
