from rest_framework import serializers
from .models import CustomUser


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('phone_number', 'email',)


class GetUserSerializer(serializers.Serializer):
    token = serializers.CharField()


class VerifyUserSerializer(serializers.Serializer):
    session_id = serializers.UUIDField()
    code = serializers.CharField(max_length=4)


class CreateTokenSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
