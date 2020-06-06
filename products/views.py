from django.shortcuts import render
from .models import Product


# --------------------------------------------------------- All products view
def all_products(request):
    """ Shows all products, including sorting and search queries. """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
