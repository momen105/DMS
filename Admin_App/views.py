from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from Login_App.models import AdminProfile,EmployeeProfile,SellerProfile
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
