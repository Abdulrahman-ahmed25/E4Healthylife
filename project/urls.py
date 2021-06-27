"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib.auth import views as auth_view


from account.views import (
    register_view,
    logout_view,
    login_view,
    buyer_register,
    seller_register,
    AccountViewsets,
    SellerViewsets,
    BuyerViewsets
)
from Hcollections.views import (
    CategoryListView,
    CategoryViewsets,
    MealcategoryViewsets,
    MealViewsets,
    HcollectionViewsets,
    UsermembershipViewsets,
    HcollectionMixinsCL,
    HcollectionMixinsRUD,

    
    )
from carts.views import (
    CartView,
    CartViewsets,
    CartitemViewsets
    )
urlpatterns = [
	path('admin/', admin.site.urls),

    # path('', CategoryListView.as_view(), name='home'),
    # path('programs/',include('programs.urls')),
    # path('categories/',include('programs.urls_categories')),
    path('', CategoryListView.as_view(), name='home'),
    path('collections/',include('Hcollections.urls')),
    path('categories/',include('Hcollections.urls_categories')),
    path('mealcategories/',include('Hcollections.urls_mealcategories')),
    path('cart/', CartView.as_view(), name='cart'),
    path('login/', login_view, name="login"), 

    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('buyer_register/',buyer_register, name='buyer_register'),
    path('seller_register/',seller_register, name='seller_register'),


]
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()

router.register('categories',CategoryViewsets)
router.register('collections',HcollectionViewsets)
router.register('mealcategories',MealcategoryViewsets)
router.register('meals',MealViewsets)
router.register('memberships',UsermembershipViewsets)
router.register('carts',CartViewsets)
router.register('cartitems',CartitemViewsets)
router.register('accounts',AccountViewsets)
router.register('sellers',SellerViewsets)
router.register('buyers',BuyerViewsets)


urlpatterns +=[
    path('api-auth/', include('rest_framework.urls')) ,
    #viewsets for all models
    path('rest/viewsets/', include(router.urls)),
    # path('api-auth', include('rest_framework.urls')),

    # Token authentication
    path('api-token-auth', obtain_auth_token, name="login"),

    #GET POST from REST framework by class based views using Mixins
        path('rest/mixinslist/', HcollectionMixinsCL.as_view()), 
        path('rest/mixinslist/<int:pk>', HcollectionMixinsRUD.as_view()), 



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)