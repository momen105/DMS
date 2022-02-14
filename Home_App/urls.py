from django.urls import path
from Home_App.views import AdminHome,SellerHome,EmplyoeeHome,Index,LoginPage


app_name = "Home_App"

urlpatterns = [
         path('', Index.as_view(), name='1st_page'),
         path('login/',LoginPage.as_view(), name='login_page'),
         path('ad_home/', AdminHome.as_view(), name='ad_home'),
         path('se_home/', SellerHome.as_view(), name='se_home'),
         path('em_home/', EmplyoeeHome.as_view(), name='em_home'),

]