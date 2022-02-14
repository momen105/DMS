from django.shortcuts import render
from Seller_App.models import Products


def product_details(request):
    product = Products.objects.all()

    return render(request, 'Seller_App/product_details.html',
                  context={'title': 'Seller', 'product': product})
