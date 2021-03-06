from django.shortcuts import render, HttpResponseRedirect
from Login_App.forms import CreateNewUser, EditAdminProfile,EditEmployeeProfile,EditSellerProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from Login_App.models import AdminProfile,EmployeeProfile,SellerProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
#from App_Posts.forms import PostForm
from Seller_App.forms import ProductsForm
from Seller_App.models import Products
from Home_App.forms import NewsForm
from Home_App.models import BreakingNews

# Create your views here.
def admin_signup(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            admin_profile = AdminProfile(user=user)
            admin_profile.save()
            return HttpResponseRedirect(reverse('Login_App:admin_login'))
    return render(request, 'Admin_App/signup.html', context={'title':'Sign up', 'form':form})

def admin_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            admin = authenticate(username=username, password=password)
            if admin is not None:
                login(request, admin)
                return HttpResponseRedirect(reverse('Login_App:ad_profile'))
    return render(request, 'Admin_App/login.html', context={'title':'Login','form':form})

@login_required
def admin_profile(request):
    seller = SellerProfile.objects.all()
    seller_count = seller.count()
    employee = EmployeeProfile.objects.all()
    employee_count = employee.count()
    product = Products.objects.all()
    product_count = product.count()
    user = User.objects.all()
    user_count = user.count()
    product_active = Products.objects.filter(public=True)
    active_count = product_active.count()
    product_rjt = Products.objects.filter(private= True)
    rjt_count =product_rjt.count()
    active = product_active.count()
    news = BreakingNews.objects.filter(public=True)
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.save()
            return HttpResponseRedirect(reverse('Login_App:ad_profile'))
    context = {'title': 'Admin',
               'seller_count': seller_count,
               'Seller': seller,
               'employee_count': employee_count,
               'product_count': product_count,
               'user_count': user_count,
               'product': product,
               'active':active,
               'form':form,
               'news':news,
               'active_count':active_count,
               'rjt_count':rjt_count}


    return render(request, 'Admin_App/profile.html',context)

@login_required
def admin_prf_edit(request):
    current_user = AdminProfile.objects.get(user=request.user)
    form = EditAdminProfile(instance=current_user)
    if request.method == 'POST':
        form = EditAdminProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditAdminProfile(instance=current_user)
            return HttpResponseRedirect(reverse('Login_App:ad_profile'))
    return render(request, 'Admin_App/edit_profile.html', context={'form': form, 'title': 'Edit Profile . Admin'})

"""""---------------------------------Seller----------------------------------"""""
def seller_signup(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            seller_profile = SellerProfile(user=user)
            seller_profile.save()
            return HttpResponseRedirect(reverse('Login_App:seller_login'))
    return render(request, 'Seller_App/signup.html', context={'title':'Sign up', 'form':form})

def seller_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            seller = authenticate(username=username, password=password)
            if seller is not None:
                login(request, seller)
                return HttpResponseRedirect(reverse('Login_App:se_profile'))
    return render(request, 'Seller_App/login.html', context={'title':'Login','form':form})

@login_required
def seller_profile(request):
    profile = SellerProfile.objects.get(user=request.user)
    form = ProductsForm()
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return HttpResponseRedirect(reverse('Home_App:se_home'))
    return render(request, 'Seller_App/profile.html', context={'title':'Seller','form':form,'profile':profile})

@login_required
def seller_prf_edit(request):
    current_user = SellerProfile.objects.get(user=request.user)
    form = EditSellerProfile(instance=current_user)
    if request.method == 'POST':
        form = EditSellerProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditSellerProfile(instance=current_user)
            return HttpResponseRedirect(reverse('Login_App:se_profile'))
    return render(request, 'Seller_App/edit_profile.html', context={'form': form, 'title': 'Edit Profile . Seller'})


"""""---------------------------------Employee----------------------------------"""""

def employee_signup(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            employee_profile = EmployeeProfile(user=user)
            employee_profile.save()
            return HttpResponseRedirect(reverse('Login_App:employee_login'))
    return render(request, 'Employee_App/signup.html', context={'title':'Sign up', 'form':form})

def employee_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            employee = authenticate(username=username, password=password)
            if employee is not None:
                login(request, employee)
                return HttpResponseRedirect(reverse('Login_App:em_profile'))
    return render(request, 'Employee_App/login.html', context={'title':'Login','form':form})

@login_required
def employee_profile(request):
    profile = EmployeeProfile.objects.get(user=request.user)
    return render(request, 'Employee_App/profile.html', context={'profile':profile})
@login_required
def employee_prf_edit(request):
    current_user = EmployeeProfile.objects.get(user=request.user)
    form = EditEmployeeProfile(instance=current_user)
    if request.method == 'POST':
        form = EditEmployeeProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditEmployeeProfile(instance=current_user)
            return HttpResponseRedirect(reverse('Login_App:em_profile'))
    return render(request, 'Employee_App/edit_profile.html', context={'form': form, 'title': 'Edit Profile . Employee'})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home_App:1st_page'))



