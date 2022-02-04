from django.contrib import admin
from .models import AdminProfile,SellerProfile,EmployeeProfile
# Register your models here.

admin.site.register(AdminProfile)
admin.site.register(SellerProfile)
admin.site.register(EmployeeProfile)