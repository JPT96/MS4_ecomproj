from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.shop, name="shop"),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateitem, name="update_item"),
    path('process_order/', views.processOrder, name='process_order')
]