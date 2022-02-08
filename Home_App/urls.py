from django.urls import path
from Home_App.views import AdminHome,SellerHome,EmplyoeeHome,Index

app_name = "Home_App"

urlpatterns = [
         path('', Index.as_view(), name='1st_page'),
         path('home/', AdminHome.as_view(), name='ad_home'),
        path('home/', SellerHome.as_view(), name='se_home'),
        path('home/', EmplyoeeHome.as_view(), name='em_home'),
]