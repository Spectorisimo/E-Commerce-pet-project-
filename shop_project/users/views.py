from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from . import services
from .models import CustomUser
from rest_framework.authtoken.models import Token
from .serializers import CreateUserSerializer,CreateTokenSerializer,GetUserSerializer


class UserViewSet(ViewSet):
    user_services: services.UserServiceInterface = services.UserServiceV1()

    def create_user(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.user_services.create_user(data=serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create_token(self, request, *args, **kwargs):
        serializer = CreateTokenSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.get(email=serializer.validated_data['email'])
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })

    def get_user(self, request, *args, **kwargs):
        serializer = GetUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = Token.objects.get(key=serializer.validated_data['token'])

        return Response({
            'email': token.user.email,
        })
