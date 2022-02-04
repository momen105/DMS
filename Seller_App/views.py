"""from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from Login_App.models import UserProfile
from django.contrib.auth.models import User

from Seller_App.models import Products
from Seller_App.forms import ProductsForm

# Create your views here.

@login_required
def seller(request):
    form = ProductsForm()
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return HttpResponseRedirect(reverse('Seller_App:seller_home'))

    post = Products.objects.all

    return render(request, 'Seller_App/profile.html', context={'title': 'Seller', 'form': form, 'post':post})
"""