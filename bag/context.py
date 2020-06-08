from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from products.models import Product


def bag_contents(request):

    bag_items = []      # Empty list for items to live in
    total = 0           # Total amount initiates at 0
    product_count = 0   # Product count initiates at 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():                   # For eac item in the bag...
        product = get_object_or_404(Product, pk=item_id)    # ... first, we get the product ...
        total += quantity * product.price                   # ... then add price of all items to the total ...
        product_count += quantity                           # ... and number of products to total count

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_TRESHOLD: # If total price is lower than the free delivery treshold
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)   # Calculates delivery amount
        free_delivery_delta = settings.FREE_DELIVERY_TRESHOLD - total   # Shows extra amount neccesary for free delivery
    else:   # If total price is larger than free delivery treshold
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_treshold': settings.FREE_DELIVERY_TRESHOLD,
        'grand_total': grand_total,
    }

    return context
