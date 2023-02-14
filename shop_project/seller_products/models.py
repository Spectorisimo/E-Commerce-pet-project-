from django.contrib.auth import get_user_model
from django.db import models
from users import choices as user_choices
from . import choices


class SellerProduct(models.Model):
    product = models.ForeignKey(
        to='products.Product',
        on_delete=models.PROTECT,
        related_name='seller_products'
    )
    seller = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        related_name='seller_products',
        limit_choices_to={'user_type': user_choices.UserTypeChoices.Seller}
    )
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    amount_currency = models.CharField(choices=choices.AmountCurrencyChoices.choices, max_length=3)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
