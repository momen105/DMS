from django import forms
#from Seller_App.models import Products
from Home_App.models import BreakingNews

class NewsForm(forms.ModelForm):
    class Meta:
        model = BreakingNews
        fields = ['title','text']
