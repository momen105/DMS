from django.urls import path
from Login_App import views

app_name = "Login_App"


urlpatterns = [
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_profile/', views.admin_profile, name='ad_profile'),
    path('admin_edit/',views.admin_prf_edit, name='admin_edit'),

    path('seller_signup/', views.seller_signup, name='seller_signup'),
    path('seller_login/', views.seller_login, name='seller_login'),
    path('seller_profile/', views.seller_profile, name='se_profile'),
    path('seller_edit/',views.seller_prf_edit, name='seller_edit'),




    path('employee_signup/', views.employee_signup, name='employee_signup'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('employee_profile/', views.employee_profile, name='em_profile'),
    path('employee_edit/',views.employee_prf_edit, name='employee_edit'),

    path('logout/',views.logout_user, name='logout'),



  #  path('edit/',views.edit_profile, name='edit'),
   # path('profile/', views.profile, name='profile'),


]