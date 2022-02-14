from django.shortcuts import render,HttpResponse
from Seller_App.models import Products
from Login_App.models import SellerProfile
from Home_App.models import BreakingNews
# Create your views here.
from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives
from DMS.settings import EMAIL_HOST_USER

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'index.html',)
class LoginPage(View):
    def get(self, request):
        return render(request, 'front_page.html',)

class AdminHome(View):
    def get(self, request):
        user = request.user
        product_post = Products.objects.filter(public=True)
        seller_list = SellerProfile.objects.all()
        return render(request, 'Admin_App/home.html',context={'title': 'Admin', 'product_post': product_post, 'seller_list': seller_list})
class SellerHome(View):
    def get(self, request):
        user = request.user
        product= Products.objects.all()
        seller_list = SellerProfile.objects.all()
        news = BreakingNews.objects.filter(public=True)

        return render(request, 'Seller_App/home.html',context={'title': 'Admin', 'product': product, 'seller_list': seller_list,'news':news})
class EmplyoeeHome(View):
    def get(self, request):
        user = request.user
        product_post = Products.objects.filter(public=True, private=False)

        seller_list = SellerProfile.objects.all()
        news = BreakingNews.objects.filter(public=True)

        return render(request, 'Employee_App/home.html',context={'title': 'Admin', 'product_post': product_post, 'seller_list': seller_list,'news':news})
