from django.urls import path
from .views import hcollection_details_view,HcollectionUpdateView #,new_user_membership

app_name='hcollections'
urlpatterns = [
    path('<int:pk>/', hcollection_details_view, name='hcollection_details'),
    # path('<int:pk>/pay', new_user_membership, name='new_user_membership'),
    path('<int:pk>/update', HcollectionUpdateView.as_view(), name='hcollection_update'),

]
