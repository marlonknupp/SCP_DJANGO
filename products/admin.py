from django.contrib import admin
from .models import Product




class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'brand', 'price')
    search_fields = ('title',)
    list_filter = ('category', 'brand')

admin.site.register(Product, ProductAdmin)