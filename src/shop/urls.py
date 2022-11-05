from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cart/', Cart.as_view(), name='cart'),
    path('categories/', Categories.as_view(), name='categories'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('contact/', Contact.as_view(), name='contact'),
    path('product/', Product.as_view(), name='product'),
]
