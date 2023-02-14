from rest_framework import serializers
from .models import Product, ProductImage


class _ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('image',)


class RetrieveProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    product_images = _ProductImageSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class _ProductSerializer(serializers.ModelSerializer):
    min_amount = serializers.DecimalField(read_only=True,decimal_places=2,max_digits=14)

    class Meta:
        model = Product
        fields = ('title', 'body', 'main_image', 'data', 'is_top', 'is_active','min_amount')


class RetrieveProductImageSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    product = _ProductSerializer(read_only=True)

    class Meta:
        model = ProductImage
        fields = '__all__'
