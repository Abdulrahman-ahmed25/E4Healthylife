from django.db import models
from Hcollections.models import Meal,Hcollection
from django.urls import reverse
from django.conf import settings

# Create your models here.
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    item = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item.title
    def get_title(self):
        return f'{self.item.title}'
    
    def get_mealList(self):
        return f'{self.item.meal_category}'
    
    # def add_to_cart(self):
    #     return 0
    def remove(self):
        return f'{reverse("cart")}?item={self.item.id}&delete=True'
        
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True, null=True,)
    items = models.ManyToManyField(Meal, through=CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
