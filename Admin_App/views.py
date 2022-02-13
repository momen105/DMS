import random

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from Login_App.models import AdminProfile, EmployeeProfile, SellerProfile
from Seller_App.models import Products
from django.views import View

from django.core.mail import EmailMultiAlternatives
from DMS.settings import EMAIL_HOST_USER
from django.views.generic import DetailView

from django.contrib.auth.decorators import login_required


# Create your views here.
def userlist(request):
    seller_list = SellerProfile.objects.all()
    employee_list = EmployeeProfile.objects.all()
    admin_list = AdminProfile.objects.all()
    return render(request, 'Admin_App/user_list.html',
                  context={'title': 'Admin', 'seller_list': seller_list, 'employee_list': employee_list,
                           'admin_list': admin_list})


def delete(request, id):
    seller = SellerProfile.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('Admin_App:user_list'))


""""def productlist(request):
    product_list = Products.objects.all()
    seller_list = SellerProfile.objects.all()

    return render(request, 'Admin_App/product_list.html', context={'title': 'Admin', 'product_list': product_list,'seller_list': seller_list})
"""


class Productlist(View):

    def get(self, request):
        user = request.user
        product_list = Products.objects.all()
        seller_list = SellerProfile.objects.all()

        return render(request, 'Admin_App/product_list.html',
                      context={'title': 'Admin', 'product_list': product_list, 'seller_list': seller_list})


def approve(request, id):
    product = Products.objects.get(id=id)
    product.public = True
    product.save()
    return HttpResponseRedirect(reverse('Admin_App:product_list'))


def product_details(request, id):
    product = Products.objects.get(id=id)

    return render(request, 'Admin_App/approve.html',
                  context={'title': 'Admin', 'product': product})


def generate_code(request,id):
    product = Products.objects.get(id=id)
    length = int((request.GET.get('length')))
    uppercase = (request.GET.get('uppercase'))
    numbers = (request.GET.get('numbers'))
    symbols = (request.GET.get('symbols'))

    chars = list('abcdefghijklmnopqrstuvwxyz')
    if (uppercase):
        chars.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if (numbers):
        chars.extend('1234567890')
    if (symbols):
        chars.extend('@!#$%^&*()_+=?><')
    thecode = ''
    for i in range(length):
        thecode += random.choice(chars)
    return render(request, 'Admin_App/code.html',
                  context={'title': 'Admin','product': product,'thecode': thecode})

def emails(request,id):
    product = Products.objects.get(id=id)
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    content = request.POST.get('content')
    msg = EmailMultiAlternatives(f'{subject}',f'{content}',EMAIL_HOST_USER,[f'{email}'])

    msg.send()
    return render(request, 'Admin_App/email.html',context={'product':product})