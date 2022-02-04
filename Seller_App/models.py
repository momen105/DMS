from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    image = models.ImageField(upload_to='products_images')
    descriptions = models.CharField(max_length=264, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date', ]