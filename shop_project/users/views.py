from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from . import services
from .models import CustomUser
from rest_framework.authtoken.models import Token
from .serializers import CreateUserSerializer, CreateTokenSerializer, GetUserSerializer, VerifyUserSerializer


class UserViewSet(ViewSet):
    user_services: services.UserServiceInterface = services.UserServiceV1()

    @swagger_auto_schema(request_body=CreateUserSerializer)
    def create_user(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.user_services.create_user(data=serializer.validated_data)
        return Response(data)

    @swagger_auto_schema(request_body=VerifyUserSerializer)
    def verify_user(self, request, *args, **kwargs):
        serializer = VerifyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.user_services.verify_user(data=serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=CreateTokenSerializer)
    def create_token(self, request, *args, **kwargs):
        serializer = CreateTokenSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        session_id = self.user_services.create_token(data=serializer.validated_data)

        return Response(session_id)

    @swagger_auto_schema(request_body=VerifyUserSerializer)
    def verify_token(self, request, *args, **kwargs):
        serializer = VerifyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = self.user_services.verify_token(data=serializer.validated_data)
        return Response(tokens)

    def get_user(self, request, *args, **kwargs):
        serializer = GetUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = Token.objects.get(key=serializer.validated_data['token'])

        return Response({
            'email': token.user.email,
        })
