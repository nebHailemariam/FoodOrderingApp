from rest_framework import serializers


class StaffProfileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, allow_null=False, allow_blank=False)
    password = serializers.CharField(max_length=128, allow_blank=False, allow_null=False)
    first_name = serializers.CharField(max_length=30, allow_blank=True)
    last_name = serializers.CharField(max_length=30, allow_blank=True)
    birth_date = serializers.DateField(allow_null=True)
    email = serializers.EmailField(allow_blank=False, allow_null=False)
    phone = serializers.CharField(max_length=255, allow_blank=True)
