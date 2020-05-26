from rest_framework.serializers import ModelSerializer
from users.models import *
from django.db import transaction


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username","password","first_name","last_name","birth_date","email","phone", "groups_id")

    def create(self, validated_data):

        user = User()
        user.username = validated_data["username"]
        user.set_password(validated_data["password"])
        user.first_name = validated_data["first_name"]
        user.last_name = validated_data["last_name"]
        user.birth_date = validated_data["birth_date"]
        user.email = validated_data["email"]
        user.phone = validated_data["phone"]
        user.groups_id = validated_data["groups_id"]
        return user


class ClientRegistrationSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=False)

    class Meta:
        model = Client
        fields = ("__all__")

    def create(self, validated_data):
        sid = transaction.savepoint()
        try:
            user_data = validated_data.pop("user")
            user_data["groups_id"] = 5
            user_account = UserSerializer.create(UserSerializer(), validated_data=user_data)
            user_account.save()
            client, created = Client.objects.update_or_create(user=user_account)
            return client
        except:
            transaction.savepoint_rollback(sid)
            raise Exception("Internal Error.")


class RestaurantAdminRegistrationSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=False)

    class Meta:
        model = RestaurantAdmin
        fields = ("__all__")

    def create(self, validated_data):
        sid = transaction.savepoint()

        try:
            user_data = validated_data.pop("user")
            user_data["groups_id"] = 4
            user_account = UserSerializer.create(UserSerializer(), validated_data=user_data)
            user_account.save()
            restaurantadmin, created = RestaurantAdmin.objects.update_or_create(user=user_account)
            return restaurantadmin
        except:
            transaction.savepoint_rollback(sid)
            raise Exception("Internal Error!")


class DeliveryManRegistrationSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=False)

    class Meta:
        model = DeliveryMan
        fields = ("__all__")

    def create(self, validated_data):
        sid = transaction.savepoint()
        try:
            user_data = validated_data.pop("user")
            user_data["groups_id"] = 3
            user_account = UserSerializer.create(UserSerializer(), validated_data=user_data)
            user_account.save()
            deliveryman, created = DeliveryMan.objects.update_or_create(user=user_account)
            return deliveryman
        except:
            transaction.savepoint_rollback(sid)
            raise Exception("Internal Error!")


