from django.shortcuts import render

from .models import Product


def home_view(request):
    render(request, 'shop/index.html')


def cart_view(request):
    render(request, 'shop/cart.html')


def categories_view(request, slug):
    render(request, 'shop/categories.html')


def checkout_view(reqeust):
    render(reqeust, 'shop/checkout.html')


def contacts_view(request):
    render(request, 'shop/contact.html')


def product_view(reqeust, pk):
    render(reqeust, 'shop/product.html')
