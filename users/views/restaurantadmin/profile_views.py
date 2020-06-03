from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.permission import IsRestaurantAdmin
from users.models import User
from users.serializers.restaurantadmin.profile_serializers import RestaurantadminProfileSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsRestaurantAdmin])
def restaurantadmin_profile(request):
    if request.method == "GET":
        serializer = RestaurantadminProfileSerializer(request.user)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = RestaurantadminProfileSerializer(data=request.data["user"])
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            user_account= request.user
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            first_name = serializer.validated_data["first_name"]
            last_name = serializer.validated_data["last_name"]
            birth_date = serializer.validated_data["birth_date"]
            email = serializer.validated_data["email"]
            phone = serializer.validated_data["phone"]

            if user_account.username != username:
                if User.objects.filter(username=username):
                    return Response("user with this username already exists",
                                    status=status.HTTP_400_BAD_REQUEST)
                user_account.username = username

            if user_account.email != email:
                if User.objects.filter(email=email):
                    return Response("user with this email already exists",
                                    status=status.HTTP_400_BAD_REQUEST)
                user_account.email = email

            user_account.set_password(password)
            user_account.first_name = first_name
            user_account.last_name = last_name
            user_account.birth_date = birth_date
            user_account.phone = phone
            user_account.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)