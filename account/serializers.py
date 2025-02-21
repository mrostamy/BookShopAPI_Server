from rest_framework import serializers
from .models import User


class SignUpSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=8,write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
