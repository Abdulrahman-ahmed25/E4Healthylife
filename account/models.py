from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class MyAccountManager(BaseUserManager):
    def create_user(self, mobile, username, password=None):
        if not mobile:
            raise ValueError("Users must have a mobile number.")
        if not username:
            raise ValueError("Users must have a username.")
        user = self.model(
            mobile = mobile,
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, mobile, username, password):
        user = self.create_user(
            mobile = mobile,
            username = username,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_seller = True
        user.is_buyer = True

        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    mobile          = PhoneNumberField(verbose_name="mobile number",unique=True)
    username        = models.CharField(max_length=30, unique=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    #our custom users
    is_seller       = models.BooleanField(default=False)
    is_buyer        = models.BooleanField(default=False)

    hide_phone      = models.BooleanField(default=True)

    objects = MyAccountManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class Seller(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username

class Buyer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username
        
#If you want every user to have an automatically generated Token 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)