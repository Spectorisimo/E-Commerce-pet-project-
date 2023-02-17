from django.urls import path
from rest_framework import routers
from ..views import OrderViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
urlpatterns = router.urls
