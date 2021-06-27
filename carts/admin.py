from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartItemInline(admin.TabularInline):
    model= CartItem
    extra = 0
class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]
    class Meta:
        Model= Cart

admin.site.register(Cart, CartAdmin)