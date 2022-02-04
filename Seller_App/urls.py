from Seller_App import views
from django.urls import path


app_name= 'Seller_App'

urlpatterns = [
    path('', views.seller, name='seller_home'),

]
