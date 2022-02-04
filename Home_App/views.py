from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, '1st_page.html',)

class Home(View):
    def get(self, request):
        return render(request, 'home.html',)