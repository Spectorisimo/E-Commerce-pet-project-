from typing import Protocol, OrderedDict

from django.db.models import QuerySet
from django.db import transaction

from . import models


class OrderRepositoryInterface(Protocol):
    @staticmethod
    def create_order(data: OrderedDict) -> models.Order:
        ...

    @staticmethod
    def get_orders() -> QuerySet[models.Order]:
        ...


class OrderRepositoryV1:
    @staticmethod
    def create_order(data: OrderedDict) -> models.Order:
        with transaction.atomic():
            order_items = data.pop('order_items')
            order = models.Order.objects.create(**data)
            models.OrderItem.objects.bulk_create([
                models.OrderItem(
                    order=order,
                    seller_product=order_item['seller_product'],
                    amount=order_item['seller_product'].amount,
                    amount_currency=order_item['seller_product'].amount_currency,
                ) for order_item in order_items
            ])

        return order

    @staticmethod
    def get_orders() -> QuerySet[models.Order]:
        return models.Order.objects.all()
