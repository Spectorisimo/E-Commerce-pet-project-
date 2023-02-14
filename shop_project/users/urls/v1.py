from django.urls import path
from .. import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('users/create/', views.UserViewSet.as_view({'post': 'create_user'})),
    path('users/verify/', views.UserViewSet.as_view({'post': 'verify_user'})),
    path('users/token/', views.UserViewSet.as_view({'post': 'create_token'})),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/token/verify/', views.UserViewSet.as_view({'post':'verify_token'})),
]
