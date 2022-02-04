from Admin_App import views
from django.urls import path


app_name= 'Admin_App'

urlpatterns = [
    path('', views.admin_page, name='Admin_page'),

]
