from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password", "email", "profile_image"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("해당 유저네임은 없습니다.")

        return data

    def get_token(self, user):
        token = super().get_token(user)
        return token


class UserPofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "profile_image"]
