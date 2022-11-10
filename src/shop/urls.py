from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('cart/', cart_view, name='cart'),
    path('categories/', categories_view, name='categories'),
    path('categories/<slug:category>/', category_view, name='category'),
    path('checkout/', checkout_view, name='checkout'),
    path('contact/', contacts_view, name='contact'),
    path('product/<int:pk>/', product_view, name='product'),
]
