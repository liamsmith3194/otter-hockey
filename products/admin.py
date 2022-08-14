from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price', 'rating', 'image',)
    ordering = ('sku',)
    list_filter = ('category', 'rating')
    search_fields = ['category', 'name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
