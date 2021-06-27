from django.contrib import admin
from .models import Hcollection, Category,Meal, Mealcategory,Usermembership
# Register your models here.
class HcollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','available_days', 'price','is_active')
admin.site.register(Hcollection, HcollectionAdmin)

admin.site.register(Category)

class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'meal_category','is_active')
admin.site.register(Meal, MealAdmin)



class MealcategoryAdmin(admin.ModelAdmin):
    list_display = ('title','category')
admin.site.register(Mealcategory, MealcategoryAdmin)

class UsermembershipAdmin(admin.ModelAdmin):
    list_display = ('user','membership')
admin.site.register(Usermembership,UsermembershipAdmin )
