from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Login_App.models import AdminProfile,SellerProfile,EmployeeProfile
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    full_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Full_name'}))
    address_1 = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'address_1'}))
    nid_number = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'nid_number'}))
    city = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'city'}))
    country = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'country'}))
    zipcode = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'zipcode'}))
    phone = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'phone'}))
    password1 = forms.CharField(
        required = True,
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required = True,
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder':'Password Confirmation'})
    )
    class Meta:
        model = User
        fields = ('email','username','full_name','nid_number','full_name','address_1','city','country','zipcode','phone','password1','password2',)

class EditAdminProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = AdminProfile()
        exclude = ('user',)

class EditEmployeeProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = EmployeeProfile()
        exclude = ('user',)

class EditSellerProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = SellerProfile()
        exclude = ('user',)
