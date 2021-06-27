from django.urls import path
from .views import CategoryListView, CategoryDetailView,HcollectionCreateView


app_name='categories'
urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='category_details'),
    path('<slug:slug>/create', HcollectionCreateView.as_view(), name='hcollection_create'),

]