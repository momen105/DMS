from Admin_App import views
from django.urls import path
from .views import Productlist

app_name= 'Admin_App'

urlpatterns = [
    path('', views.userlist, name='user_list'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('productlist/', Productlist.as_view(), name='product_list'),
    path('approve/<int:id>', views.approve, name='app'),
    path('rejected/<int:id>', views.rejected, name='rjt'),
    path('details/<int:id>', views.product_details, name='product_details'),
    path('generate_code/<int:id>', views.generate_code, name='generate_code'),
    path('sendmail/<int:id>', views.emails, name='send'),
    path('news/', views.allnews, name='allnews'),
    path('detail/<int:id>', views.detail_news, name='detail'),
    path('public/<int:id>', views.public, name='public'),
    path('hide/<int:id>', views.hide, name='hide'),

]
