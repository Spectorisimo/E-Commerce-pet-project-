from rest_framework import serializers
from .models import CustomUser


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class GetUserSerializer(serializers.Serializer):
    token = serializers.CharField()


class CreateTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
