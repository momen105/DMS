from django.urls import path
from Home_App.views import Home,Index

app_name = "Home_App"

urlpatterns = [
         path('', Index.as_view(), name='1st_page'),
         path('home/', Home.as_view(), name='home'),
]