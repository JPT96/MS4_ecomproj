from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shopper(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,)
    name= models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name =models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    
    @property
    def imageURL(self):
        try:
            url= self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Shopper, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) 
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) 
    quantity= models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Shopper, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200,null=False)
    city = models.CharField(max_length=200,null=False)
    county = models.CharField(max_length=200,null=False)
    postcode = models.CharField(max_length=200,null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
