from Employee_App import views
from django.urls import path


app_name = 'Employee_App'

urlpatterns = [
    path('conf/<int:id>', views.confirm, name='confirm'),
    path('cart/', views.cart_view, name="cart"),
    path('employee_dashboard/',views.dashboard, name= 'em_dashboard'),
    path('details/<int:id>',views.view_product, name= 'view_product'),

]
