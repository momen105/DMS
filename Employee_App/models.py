from django.db import models
from django.conf import settings
from Seller_App.models import Products
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey(Products, on_delete=models.CASCADE,related_name='cart_product')
    quantity = models.IntegerField(default=1)
    taken = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} X {self.product}'

    def get_total(self):
        total = self.product.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total

class Order(models.Model):
    orderproduct  = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderproduct.all():
            total += float(order_item.get_total())
        return total