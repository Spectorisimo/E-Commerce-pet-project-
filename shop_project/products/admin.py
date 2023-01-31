from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_top', 'is_active')
    list_filter = ('is_top', 'is_active')
    list_editable = ('is_top', 'is_active')
    search_fields = ('title', 'body')
    inlines = (ProductImageInline,)


admin.site.register(ProductImage)
