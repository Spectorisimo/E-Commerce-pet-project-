from rest_framework.routers import DefaultRouter
from .. import views
router = DefaultRouter()
router.register(r'seller_product',views.SellerProductViewSet)
urlpatterns = router.urls