from Employee_App import views
from django.urls import path


app_name = 'Employee_App'

urlpatterns = [
    path('confirm/<pk>/', views.confirm, name='confirm'),

]
