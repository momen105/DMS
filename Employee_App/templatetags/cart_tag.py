from django import template
from Employee_App.models import Order

register = template.Library()


@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
        return order[0].orderproduct.count()
    else:
        return 0