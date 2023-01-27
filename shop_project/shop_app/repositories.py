from .models import Product, ProductImage
from typing import Protocol
from django.db.models import QuerySet


class ProductRepositoryInterface(Protocol):
    @staticmethod
    def get_products() -> QuerySet[Product]:
        ...


class ProductImageRepositoryInterface(Protocol):
    @staticmethod
    def get_product_images() -> QuerySet[ProductImage]:
        ...


class ProductRepositoryV1:

    @staticmethod
    def get_products() -> QuerySet[Product]:
        return Product.objects.all().prefetch_related('product_images')


class ProductImageRepositoryV1:

    @staticmethod
    def get_product_images() -> QuerySet[ProductImage]:
        return ProductImage.objects.all().select_related('product')
