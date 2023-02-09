from typing import Protocol, OrderedDict

from rest_framework.generics import get_object_or_404

from .models import CustomUser


class UserRepositoryInterface(Protocol):
    def create_user(self, data: OrderedDict) -> CustomUser:
        ...

    def get_user(self, data: OrderedDict):
        ...


class UserRepositoryV1:
    model = CustomUser

    def create_user(self, data: OrderedDict) -> CustomUser:
        return self.model.objects.create(**data)

    def get_user(self, data: OrderedDict):
        return get_object_or_404(self.model, **data)
