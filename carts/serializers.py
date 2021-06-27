from rest_framework import serializers
from .models import  Cart,CartItem

class CartSerialization(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields='__all__'

class CartitemSerialization(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields='__all__'
