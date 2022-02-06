from Admin_App import views
from django.urls import path


app_name= 'Admin_App'

urlpatterns = [
    path('', views.userlist, name='user_list'),
    path('delete/<int:id>', views.delete, name='delete'),


]
