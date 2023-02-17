from rest_framework import serializers
from . import models


class _CreateOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ('seller_product',)


class CreateOrderSerializer(serializers.ModelSerializer):
    order_items = _CreateOrderItemSerializer(write_only=True, many=True)
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Order
        fields = (
            'customer',
            'order_items',
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'
