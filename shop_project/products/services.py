from .models import Product, ProductImage
from typing import Protocol
from django.db.models import QuerySet
from .repositories import ProductRepositoryInterface, ProductRepositoryV1, \
    ProductImageRepositoryV1, ProductImageRepositoryInterface


class ProductServiceInterface(Protocol):
    product_repository_interface: ProductRepositoryInterface

    def get_products(self):
        ...


class ProductImageServiceInterface(Protocol):
    product_image_repository_interface: ProductImageRepositoryInterface

    def get_product_images(self):
        ...


class ProductServiceV1:
    product_repository: ProductRepositoryInterface = ProductRepositoryV1()

    def get_products(self):
        return self.product_repository.get_products()


class ProductImageServiceV1:
    product_image_repository: ProductImageRepositoryInterface = ProductImageRepositoryV1()

    def get_product_images(self):
        return self.product_image_repository.get_product_images()
