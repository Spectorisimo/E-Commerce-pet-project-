from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import signals
from django.dispatch import receiver
from . import models
from users import choices as user_choices

User = get_user_model()


@receiver(signals.post_save, sender=models.Product)
def new_product_notification(sender, instance: models.Product, created: bool, **kwargs):
    if created:
        sellers = User.objects.filter(user_type=user_choices.UserTypeChoices.Seller)
        seller_emails = [seller.email for seller in sellers]
        send_mail(
            f"New product {instance.title}",
            f"Description: {instance.body}",
            settings.EMAIL_HOST_USER,
            seller_emails,
        )
