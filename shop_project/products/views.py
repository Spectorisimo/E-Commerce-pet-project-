from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from . import services
from .serializers import RetrieveProductSerializer, RetrieveProductImageSerializer
from utils import mixins
from .permissions import IsMe


class ProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZER = {
        'retrieve': RetrieveProductSerializer,
    }
    product_service: services.ProductServiceInterface = services.ProductServiceV1()
    queryset = product_service.get_products()
    serializer_class = RetrieveProductSerializer
    def get_permissions(self):
        if self.action in ('list','retrieve'):
            return AllowAny(),
        return IsMe(),



class ProductImageViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZER = {
        'retrieve': RetrieveProductImageSerializer,
    }
    product_image_service: services.ProductImageServiceInterface = services.ProductImageServiceV1()
    queryset = product_image_service.get_product_images()
    serializer_class = RetrieveProductImageSerializer
