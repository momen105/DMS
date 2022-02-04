from django.shortcuts import render
from Login_App.models import UserProfile,User

# Create your views here.
def admin_page(request):

    allprofile = UserProfile.objects.all()
    return render(request, 'admin_App/adminprofile.html', context={'title': 'admin', 'allprofile': allprofile,})
