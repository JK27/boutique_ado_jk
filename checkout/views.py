from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem, Order
from products.models import Product
from bag.contexts import bag_contents

import stripe


<<<<<<< HEAD
# --------------------------------------------------------- Checkout
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
=======
# --------------------------------------------------------- Checkout view
def checkout(request):
    stripe_public_key = 'pk_test_oiWla7xaHMF0nqAqwJQIhxGj00HLHEGeLA'    # Needs to be hidden
    stripe_secret_key = 'sk_test_g5KYB8OXEGvrHQT710wzwfWM000ymAzxlu'    # Needs to be hidden
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
<<<<<<< HEAD
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):              # If item doesn't have sizes...
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,                 # ... quantity will just be the item data
                        )
                        order_line_item.save()
                    else:                                       # If item has sizes...
                        for size, quantity in item_data['items_by_size'].items():   # ... for each item by size ...
                            order_line_item = OrderLineItem(    # ... create a line item
=======
        if order_form.is_valid():                           # If form is valid... 
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)   # ... gets item id from bag...
                    if isinstance(item_data, int):              # ... if item doesn't have sizes...
                        order_line_item = OrderLineItem(        # ... creates line item
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:                                       # ... if item has sizes...
                        for size, quantity in item_data['items_by_size'].items():   # ... for each item by size...
                            order_line_item = OrderLineItem(    # ... creates line item for each size
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
<<<<<<< HEAD
                except Product.DoesNotExist:            # In unlikely event that product doesn't exist...
                    messages.error(request, (           # ... show error message
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))
=======
                except Product.DoesNotExist:                # In the unlikely event that product is not found...
                    messages.error(request, (               # ... adds error message...
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()                          # ... deletes the empty order...
                    return redirect(reverse('view_bag'))    # ... and returns user to shopping bag page

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:                                                               # If form is not valid ...
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')                     # ... adds error message

    else:
        bag = request.session.get('bag', {})            # Gets bag from session
        if not bag:                                     # If bag is empty...
            messages.error(request,                     # ... gives error message...
                        "There is nothing in your bag at the moment")
            return redirect(reverse('products'))        # ... and redirects to products page
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


# --------------------------------------------------------- Checkout success
def checkout_success(request, order_number):
    """
<<<<<<< HEAD
    Handle successful checkouts
=======
    Handle successful checkout
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
