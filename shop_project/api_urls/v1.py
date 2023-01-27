from django.urls import path, include

urlpatterns = [
    path('', include('shop_app.urls.v1'))
]
