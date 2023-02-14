from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models

class SellerProductViewSet(ModelViewSet):
    serializer_class = serializers.SellerProductSerializer
    queryset = models.SellerProduct.objects.select_related('seller','product')