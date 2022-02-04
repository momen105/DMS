from django import forms
from Seller_App.models import Products


class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['image', 'descriptions',]