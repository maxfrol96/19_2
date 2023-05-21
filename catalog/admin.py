from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category',)
    search_fields = ('product_name', 'product_desc',)
    list_filter = ('product_category',)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'category_name')