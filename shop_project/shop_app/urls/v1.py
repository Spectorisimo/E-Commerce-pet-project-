from django.urls import path
from rest_framework import routers
from ..views import ProductViewSet, ProductImageViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
urlpatterns = router.urls
