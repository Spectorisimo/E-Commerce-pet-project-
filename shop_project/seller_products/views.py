from rest_framework.viewsets import ModelViewSet
from utils import mixins
from . import serializers
from . import models
from . import permissions


class SellerProductViewSet(mixins.ActionPermissionMixin, mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'create': serializers.CreateSellerProductSerializer,
        'update': serializers.UpdateSellerProductSerializer,
        'partial_update': serializers.UpdateSellerProductSerializer,
    }
    ACTION_PERMISSIONS = {
        'update': (permissions.IsSellerAndOwner(),),
        'partial_update': (permissions.IsSellerAndOwner(),),
        'destroy': (permissions.IsSellerAndOwner(),),
    }
    serializer_class = serializers.SellerProductSerializer
    queryset = models.SellerProduct.objects.select_related('seller', 'product')
    permission_classes = permissions.IsSellerOrReadOnly,
