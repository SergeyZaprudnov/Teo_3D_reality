from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'image', 'pub_date', 'views')
    search_fields = ('title', 'price')
    list_filter = ('title', 'pub_date', 'price')
