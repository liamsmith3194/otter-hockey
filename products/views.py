from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def stick_products(request):
    """ A view to show stick products, including sorting and search queries """

    products = Product.objects.filter(category = 1)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def bag_products(request):
    """ A view to show bag products, including sorting and search queries """

    products = Product.objects.filter(category = 2)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def clothes_products(request):
    """ A view to show clothes products, including sorting and search queries """

    products = Product.objects.filter(category = 3)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def accessories_products(request):
    """ A view to show accessories products, including sorting and search queries """

    products = Product.objects.filter(category = 4)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def all_products(request):
    """ A view to show stick products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)