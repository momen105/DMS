from django.shortcuts import render
from Login_App.models import SellerProfile,User

# Create your views here.
def admin_page(request):

    allprofile = SellerProfile.objects.all()
    return render(request, 'admin_App/adminprofile.html', context={'title': 'admin', 'allprofile': allprofile,})
