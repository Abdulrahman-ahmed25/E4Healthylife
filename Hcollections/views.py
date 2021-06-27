from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Category,Mealcategory,Hcollection, Usermembership
from account.models import Buyer
from .mixins import SellerRequiredMixmin
from .forms import UsermembershipInventoryForm
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters, mixins, generics,viewsets

# Create your views here.
class HcollectionCreateView(SellerRequiredMixmin,CreateView):
    model = Hcollection
    fields = '__all__'
    template_name = 'hcollections/hcollection_form.html'

class HcollectionUpdateView(SellerRequiredMixmin, UpdateView):
    model = Hcollection
    fields = '__all__'
    template_name = 'hcollections/hcollection_form.html'
# def usermembership_create_view(request):

def hcollection_details_view(request, pk):
    hcollection = Hcollection.objects.get(pk=pk)
    list_meals = Mealcategory.objects.filter(category = hcollection.category)
    form = UsermembershipInventoryForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'hcollection' : hcollection,
        'list_meals':list_meals,
        'form':form
    }
    return render(request, 'hcollections/hcollection_detail.html', context)

class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.filter(active=True)
    template_name = 'hcollections/category_list.html'
    

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'hcollections/category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        hcollection_set = obj.hcollection_set.all()
        context['hcollections'] = hcollection_set
        return context
        
class MealcategoryListView(ListView):
    model = Mealcategory
    queryset = Mealcategory.objects.filter(active=True)
    template_name = 'hcollections/category_list.html'
    

class MealcategoryDetailView(DetailView):
    model = Mealcategory
    template_name = 'hcollections/Mealcategory_detail.html'
    # queryset = Mealcategory.objects.filter(active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(MealcategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        meal_set = obj.meal_set.filter()
        context['meals'] = meal_set
        return context

########################### API VIEWS ###############################
class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialization
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','title']
    authentication_classes = [TokenAuthentication]
     
class HcollectionViewsets(viewsets.ModelViewSet):
    queryset = Hcollection.objects.all()
    serializer_class = HcollectionSerialization
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','title','price']
    authentication_classes = [TokenAuthentication]

# ###I do that cuz i need to customize permissions for seller to create update delete his collection to sell it
#1 - list, create
class HcollectionMixinsCL(SellerRequiredMixmin,mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Hcollection.objects.all()
    serializer_class = HcollectionSerialization
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','title','price']  
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
#2 - retrive, update, destroy
class HcollectionMixinsRUD(SellerRequiredMixmin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Hcollection.objects.all()
    serializer_class = HcollectionSerialization
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','title','price']   
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# #3 - retrive 
# class HcollectionMixinsR(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Hcollection.objects.all()
#     serializer_class = HcollectionSerialization
#     authentication_classes = [TokenAuthentication]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title','price']   

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#4 - list
# class HcollectionMixinsList(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Hcollection.objects.all()
#     serializer_class = HcollectionSerialization
#     authentication_classes = [TokenAuthentication]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title','price']  

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class MealcategoryViewsets(viewsets.ModelViewSet):
    queryset = Mealcategory.objects.all()
    serializer_class = MealcategorySerialization
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','title']
    authentication_classes = [TokenAuthentication]

class MealViewsets(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerialization
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','title']
    authentication_classes = [TokenAuthentication]

class HcollectionViewsets(viewsets.ModelViewSet):
    queryset = Hcollection.objects.all()
    serializer_class = HcollectionSerialization
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','title']
    authentication_classes = [TokenAuthentication]

class UsermembershipViewsets(viewsets.ModelViewSet):
    queryset = Usermembership.objects.all()
    serializer_class = UsermembershipSerialization
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','user']
    authentication_classes = [TokenAuthentication]

# @api_view(['POST'])
# def new_usermembership(request):
#     hcollection = Hcollection.objects.get(
#         title = request.data['title'],
#         price = request.data['price']
#     )
#     ## for create new reservation with exist guests
#     try:
#         buyer= Buyer.objects.get(
#             # usenmae = request.data['username'],
#             mobile = request.data['mobile'],
#             location = request.data['location'],
#             )
#     except Buyer.DoesNotExist:
#         raise Http404
#     reservation = Usermembership()
#     reservation.user = buyer
#     reservation.membership = hcollection
#     reservation.save()
  
#     return Response(status=status.HTTP_202_ACCEPTED)