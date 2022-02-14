from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    full_name = models.CharField(max_length=40, blank=True)
    address_1 = models.TextField(max_length=300, blank=True)
    city = models.CharField(max_length=40, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    nid_number = models.CharField(max_length=40, blank=True)
    address_1 = models.TextField(max_length=300, blank=True)
    city = models.CharField(max_length=40, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    nid_number = models.CharField(max_length=40, blank=True)
    address_1 = models.TextField(max_length=300, blank=True)
    city = models.CharField(max_length=40, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
