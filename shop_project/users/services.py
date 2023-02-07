from typing import Protocol, OrderedDict

from rest_framework_simplejwt import tokens

from .models import CustomUser
from .repositories import UserRepositoryV1, UserRepositoryInterface


class UserServiceInterface(Protocol):
    def create_user(self, data: OrderedDict) -> None:
        ...

    def create_token(self, data: OrderedDict) -> dict:
        ...


class UserServiceV1:
    user_repository: UserRepositoryInterface = UserRepositoryV1()

    def create_user(self, data: OrderedDict) -> None:
        user = self.user_repository.create_user(data=data)
        self._send_email(user.email)

    def create_token(self, data: OrderedDict) -> dict:
        user = self.user_repository.get_user(data=data)
        access = tokens.AccessToken.for_user(user=user)
        refresh = tokens.RefreshToken.for_user(user=user)
        return {
            'access': str(access),
            'refresh': str(refresh),
        }

    @staticmethod
    def _send_email(email: str) -> None:
        print(f'send email to {email}')
