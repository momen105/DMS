from django import forms
from Payment_App.models import BillingAddress



class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address', 'zipcode','security_code', 'city', 'country']