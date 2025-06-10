from django.contrib import admin
from .models import Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at']
    inlines = [OrderItemInline]


# products/admin.py
from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)
