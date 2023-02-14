import uuid
from typing import Protocol, OrderedDict
from django.core.mail import send_mail
from rest_framework_simplejwt import tokens
from django.core.cache import cache
from .models import CustomUser
from .repositories import UserRepositoryV1, UserRepositoryInterface
import random
from django.conf import settings


class UserServiceInterface(Protocol):

    def create_user(self, data: OrderedDict) -> None:
        ...

    def verify_user(self, data: OrderedDict) -> None:
        ...

    def create_token(self, data: OrderedDict) -> dict:
        ...

    def verify_token(self, data: OrderedDict) -> dict:
        ...


class UserServiceV1:
    user_repository: UserRepositoryInterface = UserRepositoryV1()

    def create_user(self, data: OrderedDict) -> None:
        session_id = self._verify_phone_number(data)
        return {
            'session_id': session_id,
        }

    def create_token(self, data: OrderedDict) -> dict:
        session_id = self._verify_phone_number(data)
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

    def verify_token(self, data: OrderedDict) -> CustomUser | None:
        session = cache.get(data['session_id'])
        if not session:
            return

        if session['code'] != data['code']:
            return

        user = self.user_repository.get_user(data=
                                             {'phone_number': session['phone_number'],
                                              })
        access = tokens.AccessToken.for_user(user=user)
        refresh = tokens.RefreshToken.for_user(user=user)

        return {
            'access': str(access),
            'refresh': str(refresh),
        }

    def _verify_phone_number(self, data: OrderedDict, is_exist: bool = None) -> str:
        phone_number = data['phone_number']
        if is_exist:
            user = self.user_repos.get_user(data)
            phone_number = str(user.phone_number)

        code = self._generate_code()
        session_id = self._generate_session_id()
        cache.set(session_id, {'phone_number': phone_number, 'code': code, **data}, timeout=300)
        self._send_sms(phone_number=data['phone_number'], code=code)
        return session_id

    @staticmethod
    def _generate_code(lenght: int = 4) -> str:

        numbers = [str(i) for i in range(10)]
        code = ''.join(random.choices(numbers, k=lenght))
        return code

    @staticmethod
    def _generate_session_id() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def _send_email(email: str) -> None:
        subject = "Registration"
        message = "Thanks for registration in our website"
        send_mail(subject=subject,
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[email, ])

    @staticmethod
    def _send_sms(phone_number: str, code: str) -> None:
        print(f"SMS Code - {code} has been sent to {phone_number}")
