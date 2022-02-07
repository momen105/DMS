from django import forms
from Seller_App.models import Products


class ApproveForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['private',]