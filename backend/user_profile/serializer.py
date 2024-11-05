from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "profile_pic",
        ]
        read_only_fields = ["id", "user"]

        def update(self, instance, validated_data):
            user = self.context["request"].user
            if user != instance.user:
                raise serializers.ValidationError(
                    {"detail": "You do not have permission to perform this action"}
                )
            instance.avatar_url = validated_data.get("avatar_url", instance.avatar_url)
            instance.save()
            return instance
