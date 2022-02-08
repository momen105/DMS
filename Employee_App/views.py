from django.shortcuts import render
from Seller_App.models import Products
from Seller_App.models import ConfirmProduct
from django.shortcuts import render, HttpResponseRedirect,reverse

# Create your views here.
def confirm(request, pk):
    product = Products.objects.get(pk=pk)
    confirm = ConfirmProduct.objects.filter(product=product, user=request.user)
    confirm.save()
    return HttpResponseRedirect(reverse('Home_App:ad_home'))
