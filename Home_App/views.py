from django.shortcuts import render
from Seller_App.models import Products
from Login_App.models import SellerProfile
# Create your views here.
from django.views import View
from django.shortcuts import render

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, '1st_page.html',)

class Home(View):
    def get(self, request):
        user = request.user
        product_post = Products.objects.filter(public=True)
        seller_list = SellerProfile.objects.all()

        return render(request, 'home.html',
                      context={'title': 'Admin', 'product_post': product_post, 'seller_list': seller_list})
