from Seller_App import views
from django.urls import path


app_name = 'Seller_App'

urlpatterns = [
    path('product_details/', views.product_details, name='product_details'),


]
