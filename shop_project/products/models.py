from django.contrib.auth import get_user_model
from django.db import models
import uuid

from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=255, verbose_name=_('Title'), unique=True)
    body = models.TextField(verbose_name=_('Body'))
    main_image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name=_('Main Image'))
    data = models.JSONField(default=dict, verbose_name=_('Data'))
    is_top = models.BooleanField(default=False, verbose_name=_('Is top?'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active?'))
    user = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('is_top', '-created_at',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    image = models.ImageField(upload_to='product-images/%Y/%m/%d/', verbose_name=_('Image'))
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='product_images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
