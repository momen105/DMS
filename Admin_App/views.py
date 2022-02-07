from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from Login_App.models import AdminProfile,EmployeeProfile,SellerProfile
from Seller_App.models import Products
from django.views import View

from django.views.generic import DetailView

from django.contrib.auth.decorators import login_required

# Create your views here.
def userlist(request):
    seller_list = SellerProfile.objects.all()
    employee_list = EmployeeProfile.objects.all()
    admin_list = AdminProfile.objects.all()
    return render(request, 'Admin_App/user_list.html', context={'title': 'Admin', 'seller_list': seller_list,'employee_list':employee_list,'admin_list':admin_list })

def delete(request,id):
    seller = SellerProfile.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('Admin_App:user_list'))

""""def productlist(request):
    product_list = Products.objects.all()
    seller_list = SellerProfile.objects.all()

    return render(request, 'Admin_App/product_list.html', context={'title': 'Admin', 'product_list': product_list,'seller_list': seller_list})
"""

class Productlist(View):

    def get(self,request):
        user = request.user
        product_list = Products.objects.all()
        seller_list = SellerProfile.objects.all()

        return render(request, 'Admin_App/product_list.html',
                      context={'title': 'Admin', 'product_list': product_list, 'seller_list': seller_list})

def approve(request,id):
    product = Products.objects.get(id=id)
    product.public = True
    product.save()
    return HttpResponseRedirect(reverse('Admin_App:product_list'))
