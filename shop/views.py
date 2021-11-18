from django.shortcuts import render
from .models import *
# Create your views here.
def shop(request):
    products = Product.objects.all()
    context = {'products':products}
    return render (request, 'shop/shop.html', context)

def cart(request):

    if request.user.is_autheticated:
        shopper = request.user.shopper
        order, created = Order.objects.get_or_create(shopper=shopper, complete=False)
        item = order.orderitem_set.all()
    else:
        items = []
    context = {}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)

