from django.contrib import admin
from .models import Product, Category


# --------------------------------------------------------- PRODUCT ADMIN
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


# --------------------------------------------------------- CATEGORY ADMIN
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
