from django.views.generic import ListView, TemplateView

from .models import Product


class Home(ListView):
    model = Product
    template_name = 'shop/index.html'


class Cart(TemplateView):
    template_name = 'shop/cart.html'


class Categories(TemplateView):
    template_name = 'shop/categories.html'


class Checkout(TemplateView):
    template_name = 'shop/checkout.html'


class Contact(TemplateView):
    template_name = 'shop/contact.html'


class Product(TemplateView):
    template_name = 'shop/product.html'
