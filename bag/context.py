from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from products.models import Product


def bag_contents(request):

    bag_items = []      # Empty list for items to live in
    total = 0           # Total amount initiates at 0
    product_count = 0   # Product count initiates at 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():                      # For each item in the bag...
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)    # ... first, we get the product ...
            total += item_data * product.price                  # ... then add price of all items to the total ...
            product_count += item_data                          # ... and number of products to total count

            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity

                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'size': size,
            })

    if total < settings.FREE_DELIVERY_TRESHOLD:     # If total price is lower than the free delivery treshold
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
