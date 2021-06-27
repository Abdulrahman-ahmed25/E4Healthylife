from django.urls import path
from .views import MealcategoryListView, MealcategoryDetailView


app_name='mealcategories'
urlpatterns = [
    path('', MealcategoryListView.as_view(), name='mealcategories'),
    path('<slug:slug>/', MealcategoryDetailView.as_view(), name='mealcategory_details'),

]