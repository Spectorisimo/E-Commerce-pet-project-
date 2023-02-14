from django.db import models


class AmountCurrencyChoices(models.TextChoices):
    USD = 'USD'
    KZT = 'KZT'
    EUR = 'EUR'
    RUB = 'RUB'
