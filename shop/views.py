from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
# Create your views here.
def shop(request):


    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:

        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = ['get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render (request, 'shop/shop.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = ['get_cart_items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = ['get_cart_items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
     
    return render(request, 'shop/checkout.html', context)

def updateitem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created =  OrderItem.objects.get_or_create(order = order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('add has been added', safe = False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.shipping == True:
            shippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data ['shipping']['address'],
                city = data ['shipping']['city'],
                county = data ['shipping']['county'],
                postcode = data ['shipping']['postcode'],
                country = data ['shipping']['country'],
            )
        else:
            print('user is not signed in')
        return JsonResponse('Your order is on the way', safe = False) 








    