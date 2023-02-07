from rest_framework.permissions import BasePermission
from .models import Product

class IsMe(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user
                    and request.user.is_authenticated
                    )
    def has_object_permission(self, request, view, obj: Product):
        return obj.user == request.user
