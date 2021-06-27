from rest_framework import serializers
from .models import  Meal, Category, Hcollection, Mealcategory, Usermembership

class CategorySerialization(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'

class HcollectionSerialization(serializers.ModelSerializer):
    class Meta:
        model = Hcollection
        fields='__all__'

class MealcategorySerialization(serializers.ModelSerializer):
    class Meta:
        model = Mealcategory
        fields='__all__'

class MealSerialization(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields='__all__'

class UsermembershipSerialization(serializers.ModelSerializer):
    class Meta:
        model = Usermembership
        fields='__all__'