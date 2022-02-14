from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages
#models and forms
from Employee_App.models import Order, Cart
from Payment_App.forms import BillingAddress
from Payment_App.forms import BillingForm


from django.contrib.auth.decorators import login_required

# for payment
import requests
from decimal import Decimal
from sslcommerz_python_api.payment import SSLCSession
import socket
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    print(saved_address)
    form = BillingForm()
    if request.method == "POST":
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    #print(order_qs)
    order_product = order_qs[0].orderproduct.all()
    #print(order_items)
    order_total = order_qs[0].get_totals()
    return render(request, 'checkout.html', context={"form":form, "order_items":order_product, "order_total":order_total, "saved_address":saved_address})

@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_filled():
        return redirect("Payment_App:checkout")



    store_id = 'dms6207d2d48ad46'
    API_key = 'dms6207d2d48ad46@ssl'

    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)

    status_url = request.build_absolute_uri(reverse("Payment_App:complete"))
    #print(status_url)
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_product = order_qs[0].orderproduct.all()
    order_product_count = order_qs[0].orderproduct.count()
    order_total = order_qs[0].get_totals()

    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='Mixed', product_name=order_product, num_of_item=order_product_count, shipping_method='Courier', product_profile='None')


    current_user = request.user
    mypayment.set_customer_info(name=current_user.employee_profile.full_name, email=current_user.email, address1=current_user.employee_profile.address_1, address2=current_user.employee_profile.address_1, city=current_user.employee_profile.city, postcode=current_user.employee_profile.zipcode, country=current_user.employee_profile.country, phone=current_user.employee_profile.phone)

    mypayment.set_shipping_info(shipping_to=current_user.employee_profile.full_name, address=saved_address.address, city=saved_address.city, postcode=saved_address.zipcode, country=saved_address.country)

    response_data = mypayment.init_payment()
    return redirect(response_data['GatewayPageURL'])


@csrf_exempt
def complete(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']

        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            return HttpResponseRedirect(reverse("Payment_App:purchase", kwargs={'val_id':val_id, 'tran_id':tran_id},))
        elif status == 'FAILED':
            messages.warning(request, f"Your Payment Failed! Please Try Again! Page will be redirected!")

    return render(request, "complete.html", context={})

@login_required
def purchase(request, val_id, tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    orderId = tran_id
    order.ordered = True
    order.orderId = orderId
    order.paymentId = val_id
    order.save()
    cart_items = Cart.objects.filter(user=request.user, taken=False)
    for item in cart_items:
        item.taken = True
        item.save()
    return HttpResponseRedirect(reverse("Login_App:em_profile"))

@login_required
def order_view(request):
    try:
        orders = Order.objects.filter(user=request.user, ordered=True)
        context = {"orders": orders}
    except:
        return redirect("Login_App:em_profile")
    return render(request, "Employee_App/order.html", context)