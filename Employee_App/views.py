from django.shortcuts import render, HttpResponseRedirect,reverse
from django.shortcuts import render, get_object_or_404, redirect

# Authentications
from django.contrib.auth.decorators import login_required

# Model
from Seller_App.models import ConfirmProduct
from Employee_App.models import Cart, Order
from Seller_App.models import Products



# Create your views here.
def dashboard(request):


    return render(request, 'Employee_App/dashboard.html')


@login_required
def confirm(request, id):
    product = get_object_or_404(Products, id=id)
    order_product = Cart.objects.get_or_create(product=product, user=request.user, taken=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    #print(order_qs[0])
    if order_qs.exists():
        order = order_qs[0]
        if order.orderproduct.filter(product=product).exists():
            order_product[0].quantity += 1
            order_product[0].save()
            return redirect("Home_App:em_home")
        else:
            order.orderproduct.add(order_product[0])
            return redirect("Home_App:em_home")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderproduct.add(order_product[0])
        return redirect("Home_App:em_home")

@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, taken=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'Employee_App/cart_view.html', context={'carts':carts, 'order':order})
    else:
        return redirect("Home_App:em_home")
