from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(
            PostManager,
            self).filter(draft=False).filter(publish__lte=timezone.now())

    def public_post(self, *args, **kwargs):
        return super(
            PostManager,
            self).filter(public=True)

    def private_post(self, *args, **kwargs):
        return super(
            PostManager,
            self).filter(public=False)

class Products(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    image = models.ImageField(upload_to='products_images')
    descriptions = models.CharField(max_length=264, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=True)


    objects = PostManager()

    @property
    def is_public(self):
        return self.public

    @property
    def is_private(self):
        return self.private


    class Meta:
        ordering = ['-upload_date', ]