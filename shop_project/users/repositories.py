from typing import Protocol, OrderedDict
from .models import CustomUser


class UserRepositoryInterface(Protocol):
    def create_user(self, data: OrderedDict) -> CustomUser:
        ...


class UserRepositoryV1:
    model = CustomUser

    def create_user(self, data: OrderedDict) -> CustomUser:
        return self.model.objects.create(**data)
