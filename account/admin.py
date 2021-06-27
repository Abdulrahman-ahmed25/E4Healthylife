from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Buyer, Seller

class AccountAdmin(UserAdmin):
    list_display = ('mobile', 'username', 'is_admin', 'is_staff','is_seller','is_buyer')
    search_fields= ('mobile', 'username')
    readonly_fields = ['id','last_login']
    filter_horizontal=()
    list_filter=()
    fieldsets = ()
admin.site.register(Account, AccountAdmin)

class BuyerAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')
admin.site.register(Buyer, BuyerAdmin)

class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')
admin.site.register(Seller, SellerAdmin)