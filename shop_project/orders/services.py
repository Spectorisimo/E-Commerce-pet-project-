from typing import Protocol, OrderedDict
from django.db.models import QuerySet
from . import models, repositories


class OrderServicesInterface(Protocol):

    def create_order(self, data: OrderedDict) -> models.Order:
        ...

    def get_orders(self) -> QuerySet[models.Order]:
        ...


class OrderServicesV1:
    order_repository: repositories.OrderRepositoryInterface = repositories.OrderRepositoryV1()

    def create_order(self, data: OrderedDict) -> models.Order:
        return self.order_repository.create_order(data=data)

    def get_orders(self) -> QuerySet[models.Order]:
        return self.order_repository.get_orders()
