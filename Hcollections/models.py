from django.db import models
from django.urls import reverse
from account.models import Buyer
from django.db.models.signals import post_save
# Create your models here.
class Category(models.Model):
    title           = models.CharField(max_length=120, unique=True, null=False, blank=False)
    slug            = models.SlugField(unique=True)
    description     = models.TextField(null=True, blank=True)
    active          = models.BooleanField(default=True)
    time_published  = models.DateTimeField(auto_now_add=True, auto_now=False)
    image           = models.ImageField(upload_to = 'images/category_images', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("categories:category_details", kwargs = {"slug": self.slug})

class Hcollection(models.Model):
    title           = models.CharField(max_length=120,null=False, blank=False, unique=True)
    description     = models.TextField(blank=True, null=True)
    price           = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    available_days  = models.IntegerField(blank=False, null=False)
    is_active       = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    hcollection_image   = models.ImageField(max_length=255, upload_to='images/hcollection_images', null=True, blank=True,)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("hcollections:hcollection_details", kwargs = {"pk": self.pk})


class Mealcategory(models.Model):
    title           = models.CharField(max_length=120, unique=True, null=False, blank=False)
    slug            = models.SlugField(unique=True)
    active          = models.BooleanField(default=True)
    time_published  = models.DateTimeField(auto_now_add=True, auto_now=False)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("mealcategories:mealcategory_details", kwargs = {"slug": self.slug})
        
class Meal(models.Model):
    title                = models.CharField(max_length=120,null=False, blank=False)
    description          = models.TextField(blank=True, null=True)
    meal_image           = models.ImageField(upload_to = 'images/meal_images', null=True)
    is_active            = models.BooleanField(default=True)
    meal_category        = models.ForeignKey(Mealcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Usermembership(models.Model):
    user        = models.OneToOneField(Buyer, on_delete=models.CASCADE, related_name='reservation')
    membership  = models.ForeignKey(Hcollection, on_delete=models.CASCADE, related_name='reservation')
    def __str__(self):
        return f'{self.user}-{self.membership}'

    def get_membership_title(self):
        return self.membership.title  
          
    def get_available_days(self):
        return self.membership.available_days
        
    def get_price(self):
        return self.membership.price

# def usermembership_saved_receiver(sender, instance,created, *args, **kwargs):
#     hcollection = instance
#     usermemberships = hcollection.usermembership_set.all()
#     if usermemberships.count() == 0:
#         usermembership = Usermembership()
#         usermembership.hcollection = hcollection
#         usermembership.title = hcollection.title
#         usermembership.price = hcollection.price
#         usermembership.save()

# post_save.connect(usermembership_saved_receiver, sender=Buyer)

# def post_save_usermembership_create(sender,instance,created, *args, **kwargs):
#     if created:
#         Usermembership.objects.get_or_create(user=instance)
#     user_membership, created = Usermembership.objects.get_or_create(user=instance)
#     if user_membership.customer_id is None or user_membership.customer_id == '':
#         new_customer_id = stripe.Customer.create(mobile=instance.mobile)
#         user_membership.customer_id = new_customer_id['id']
#         user_membership.save()
# post_save.connect(post_save_usermembership_create, sender=Buyer)

# class Subscription(models.Model):
#     user_membership = models.ForeignKey(Usermembership, on_delete=models.CASCADE)
#     active          = models.BooleanField(default=True)
#     def __str__(self):
#         return self.user_membership.user.username
