from rest_framework import serializers
from .models import Seller,Buyer, Account

class AccountSerialization(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = Account
        fields='__all__'

class SellerSerialization(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields='__all__'

class BuyerSerialization(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields='__all__'