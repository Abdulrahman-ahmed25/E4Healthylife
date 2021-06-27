from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .models import Account, Seller,Buyer
from django.views.generic import CreateView
from .forms import SellerSignUpForm,RegistrationForm,AccountAuthenticationForm, SellerSignUpForm,BuyerSignUpForm
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters, mixins, generics,viewsets


# def register_view(request, *args, **kwargs):
# 	user = request.user
# 	if user.is_authenticated: 
# 		return HttpResponse("You are already authenticated as " + str(user.mobile))

# 	context = {}
# 	if request.POST:
# 		form = RegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			mobile = form.cleaned_data.get('mobile')
# 			raw_password = form.cleaned_data.get('password1')
# 			account = authenticate(mobile=mobile, password=raw_password)
# 			login(request, account)
# 			destination = kwargs.get("next")
# 			if destination:
# 				return redirect(destination)
# 			return redirect('home')
# 		else:
# 			context['registration_form'] = form

# 	else:
# 		form = RegistrationForm()
# 		context['registration_form'] = form
# 	return render(request, 'account/register.html', context)
def register_view(request):
	return render(request, 'account/firstregister.html',{})
def buyer_register(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.mobile))

	context = {}
	if request.POST:
		form = BuyerSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			mobile = form.cleaned_data.get('mobile')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(mobile=mobile, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = BuyerSignUpForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)
def seller_register(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.mobile))

	context = {}
	if request.POST:
		form = SellerSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			mobile = form.cleaned_data.get('mobile')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(mobile=mobile, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = SellerSignUpForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)

def logout_view(request):
	logout(request)
	return redirect("home")


def login_view(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	destination = get_redirect_if_exists(request)
	print("destination: " + str(destination))

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			mobile = request.POST['mobile']
			password = request.POST['password']
			user = authenticate(mobile=mobile, password=password)

			if user:
				login(request, user)
				if destination:
					return redirect(destination)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "account/login.html", context)


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect

######################## API VIEW ##############################
class AccountViewsets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerialization
    filter_backends = [filters.SearchFilter]
    search_fields = ['mobile','username']
    authentication_classes = [TokenAuthentication]

class SellerViewsets(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerialization
    filter_backends = [filters.SearchFilter]
    search_fields = ['mobile','username']
    authentication_classes = [TokenAuthentication]

class BuyerViewsets(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerialization
    filter_backends = [filters.SearchFilter]
    search_fields = ['mobile','username']
    authentication_classes = [TokenAuthentication]