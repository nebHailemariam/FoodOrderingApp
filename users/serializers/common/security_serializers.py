from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from users.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username is not None or password is not None:
            user = authenticate(username=username, password=password)
            if user:
                data["user"] = user
                return data
            user_instance = User.objects.filter(username=username, password=password).first()
            if user_instance is not None:
                if not user_instance.is_active:
                    raise exceptions.ValidationError("User not activated yet.")
                data["user"] = user_instance
                return data
            else:
                raise exceptions.ValidationError("Invalid credentials.")
        else:
            raise exceptions.ValidationError("Username and password must be provided.")
