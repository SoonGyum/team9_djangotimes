from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "profile_image",
            "introductions",
            "created_at",
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("id")
        return ret
