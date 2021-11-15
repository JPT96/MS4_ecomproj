from django.db import models
from django.contrib.auth.models import user
# Create your models here.

class Shopper(models.model):
    user= models.OneToOneField(User, on_delete=models.CASCADE null=True, blank=True, on_delete = models.CASCADE)
    name= models.CharField(max_length=200, null=True)
    email=model.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.model):
    name =models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.model):
    customer = models.ForeginKey(Customer, on_delete=models.set_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.model):
    product = models.ForeginKey(Product, on_delete=models.set_NULL, null=True) 
    order = models.ForeginKey(Order, on_delete=models.set_NULL, null=True) 
    quantity= models.IntergerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
