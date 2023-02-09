import uuid
from typing import Protocol, OrderedDict

from rest_framework_simplejwt import tokens
from django.core.cache import cache
from .models import CustomUser
from .repositories import UserRepositoryV1, UserRepositoryInterface
import random
import requests

class UserServiceInterface(Protocol):

    def create_user(self, data: OrderedDict) -> None:
        ...

    def verify_user(self, data: OrderedDict) -> None:
        ...

    def create_token(self, data: OrderedDict) -> dict:
        ...


class UserServiceV1:
    user_repository: UserRepositoryInterface = UserRepositoryV1()

    def create_user(self, data: OrderedDict) -> None:
        numbers = [str(i) for i in range(10)]
        code = ''.join(random.choices(numbers, k=4))
        session_id = str(uuid.uuid4())
        data = {
            'code': code, **data,
        }
        cache.set(session_id, data, timeout=300)
        self._send_sms(phone_number=data['phone_number'], code=code)
        return {
            'session_id': session_id,
        }

    def verify_user(self, data: OrderedDict) -> CustomUser | None:
        user_data = cache.get(data['session_id'])
        if not user_data:
            return
        if data['code'] != user_data['code']:
            return
        user = self.user_repository.create_user(data={
            'email': user_data['email'],
            'phone_number': user_data['phone_number']
        })
        self._send_email(email=user.email)


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

    @staticmethod
    def _send_sms(phone_number: str, code: str) -> None:
        print(f"SMS Code - {code} has been sent to {phone_number}")
