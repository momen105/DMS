from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BreakingNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='breaking_news')
    title = models.CharField(max_length=30, blank=True)
    text = models.CharField(max_length=264, blank=True)
    public = models.BooleanField(default=True)
    hide = models.BooleanField(default=False)