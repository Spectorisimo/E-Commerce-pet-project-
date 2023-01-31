from typing import Protocol, OrderedDict
from .models import CustomUser
from .repositories import UserRepositoryV1, UserRepositoryInterface


class UserServiceInterface(Protocol):
    def create_user(self, data: OrderedDict) -> None:
        ...


class UserServiceV1:
    user_repository:UserRepositoryInterface = UserRepositoryV1()

    def create_user(self, data: OrderedDict) -> None:
        user = self.user_repository.create_user(data=data)
        self._send_email(user.email)

    @staticmethod
    def _send_email(email: str) -> None:
        print(f'send email to {email}')


