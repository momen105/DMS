from django.shortcuts import render, HttpResponseRedirect
from Login_App.forms import CreateNewUser, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from Login_App.models import AdminProfile,EmployeeProfile,SellerProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

#from App_Posts.forms import PostForm
from django.contrib.auth.models import User


# Create your views here.
def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Login_App:login'))
    return render(request, 'Login_App/signup.html', context={'title':'Sign up', 'form':form})

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Home_App:home'))
    return render(request, 'Login_App/login.html', context={'title':'Login','form':form})

@login_required
def edit_profile(request):
    if request.user == True:
        current_user = UserProfile.objects.getgit(user=request.user)
        form = EditProfile(instance=current_user)
        if request.method == 'POST':
            form = EditProfile(request.POST, request.FILES, instance=current_user)
            if form.is_valid():
                form.save(commit=True)
                form = EditProfile(instance=current_user)
                return HttpResponseRedirect(reverse('Login_App:profile'))
        return render(request, 'Login_App/profile.html', context={'form': form, 'title': 'Edit Profile . Social'})
    else:
        current_user = User.objects.get(id=1)
        form = EditProfile(instance=current_user)
        if request.method == 'POST':
            form = EditProfile(request.POST, request.FILES, instance=current_user)
            if form.is_valid():
                form.save(commit=True)
                form = EditProfile(instance=current_user)
                return HttpResponseRedirect(reverse('Login_App:profile'))
        return render(request, 'Login_App/profile.html', context={'form': form, 'title': 'Edit Profile . Social'})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_App:login'))

#@login_required
#def profile(request):
  #  return render(request, 'Login_App/user.html', context={'title':'User'})