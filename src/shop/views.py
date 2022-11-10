from django.shortcuts import render

from .models import Product, Category


def home_view(request):
    products = Product.objects.all()[:8]
    context = {
        'categories': Category.objects.all(),
        'products': products
    }
    return render(request, 'shop/index.html', context)


def cart_view(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'shop/cart.html', context)


def categories_view(request):
    products = Product.objects.all()
    context = {
        'categories': Category.objects.all(),
        'products': products
    }
    return render(request, 'shop/categories.html', context)


def category_view(request, category):
    products = Product.objects.filter(category__slug=category)
    category = Category.objects.get(slug=category)
    context = {
        'category': category,
        'categories': Category.objects.all(),
        'products': products
    }
    return render(request, 'shop/categories.html', context)


def checkout_view(reqeust):
    context = {
        'categories': Category.objects.all(),
    }
    return render(reqeust, 'shop/checkout.html', context)


def contacts_view(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'shop/contact.html', context)


def product_view(reqeust, pk):
    product = Product.objects.get(pk=pk)
    related_products = Product.objects.all()[:4]
    context = {
        'categories': Category.objects.all(),
        'product': product,
        'related_products': related_products,
    }
    return render(reqeust, 'shop/product.html', context)
