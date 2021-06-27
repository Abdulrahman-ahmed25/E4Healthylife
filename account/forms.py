# from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from phonenumber_field.formfields import PhoneNumberField
from .models import Account, Seller,Buyer
from django.db import transaction

class RegistrationForm(UserCreationForm):
	mobile = PhoneNumberField(max_length=50, help_text='Required. Add a valid mobile number.')

	class Meta:
		model = Account
		fields = ('mobile', 'username', 'password1', 'password2', )

	def clean_mobile(self):
		mobile = self.cleaned_data['mobile']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(mobile=mobile)
		except Account.DoesNotExist:
			return mobile
		raise forms.ValidationError('mobile "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('mobile', 'password')

	def clean(self):
		if self.is_valid():
			mobile = self.cleaned_data['mobile']
			password = self.cleaned_data['password']
			if not authenticate(mobile=mobile, password=password):
				raise forms.ValidationError("Invalid login")
				
class SellerSignUpForm(RegistrationForm):
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = Account

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.mobile = self.cleaned_data.get('mobile')
        user.username = self.cleaned_data.get('username')
        user.save()
        seller = Seller.objects.create(user=user)
        seller.location=self.cleaned_data.get('location')
        seller.save()
        return user

class BuyerSignUpForm(RegistrationForm):
    location = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = Account
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_buyer = True
        user.mobile = self.cleaned_data.get('mobile')
        user.username = self.cleaned_data.get('username')
        user.save()
        buyer = Buyer.objects.create(user=user)
        buyer.location=self.cleaned_data.get('location')
        buyer.save()
        return user