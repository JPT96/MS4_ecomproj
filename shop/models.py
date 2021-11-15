from django.db import models
from django.contrib.auth.models import user
# Create your models here.

class Shopper(models.model):
    user= models.OneToOneField(User, null=True, blank=True, on_delete = models.CASCADE)
    name= models.CharField(max_length=200, null=True)
    email=model.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name