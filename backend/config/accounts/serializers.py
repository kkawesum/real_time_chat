from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = User
        fields = (
            "id",
            "phone_number",
            "first_name",
            "last_name",
            "profile_picture",
            "about",
            "is_online",
            "last_seen",
        )

        read_only_fields = (
            "id",
            "last_seen",
            "is_online",
        )


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields = [
            "phone_number",
            "first_name",
            "last_name",
            "password",
        ]

    def create(self, validated_data):

        password = validated_data.pop("password")

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        return user

class LoginSerializer(serializers.Serializer):

    phone_number = serializers.CharField()

    password = serializers.CharField()

    def validate(self, attrs):

        request = self.context.get("request")

        user = authenticate(
            request=request,
            phone_number=attrs["phone_number"],
            password=attrs["password"],
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        attrs["user"] = user

        return attrs

