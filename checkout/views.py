from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})            # Gets bag from session
    if not bag:                                     # If bag is empty...
        messages.error(request,                     # ... gives error message...
                       "There is nothing in your bag at the moment")
        return redirect(reverse('products'))        # ... and redirects to products page

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_oiWla7xaHMF0nqAqwJQIhxGj00HLHEGeLA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
