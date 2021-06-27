from django import forms
from .models import Usermembership
from django.contrib.auth.forms import User
class UsermembershipInventoryForm(forms.ModelForm):
    users = User
           
    class Meta:
        model = Usermembership
        fields = [
            'user',
            "membership",
        ]
    
