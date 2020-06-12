from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


# --------------------------------------------------------- View Bag contents
def view_bag(request):
    """ Renders bag contents page """
    return render(request, 'bag/bag.html')


# --------------------------------------------------------- Add contents to bag
def add_to_bag(request, item_id):
    """ Adds quantity of specified product to shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))    # Needs conversion to int as comes as string from from
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})    # Keeps bag contents while session lasts. If not session, it creates one

    if size:                                                        # If product has sizes...
        if item_id in list(bag.keys()):                             # ... and if product is already in bag...
            if size in bag[item_id]['items_by_size'].keys():        # ... and if it has same size...
                bag[item_id]['items_by_size'][size] += quantity     # ... then update quantity accordingly...
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}.')
            else:                                                   # ... but if it has a different size...
                bag[item_id]['items_by_size'][size] = quantity      # ... then add quantity of items of that size
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag.')
        else:                                                       # But if product is not already in bag...
            bag[item_id] = {'items_by_size': {size: quantity}}      # ... adds quantity of items of each size to bag
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag.')
    else:                                   # If product does not have sizes...
        if item_id in list(bag.keys()):     # ...and if item already exists in bag ...
            bag[item_id] += quantity        # ...updates quantity accordingly
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}.')
        else:                               # But if item not alreay in bag ...
            bag[item_id] = quantity         # ... adds specified quantity of items to bag
            messages.success(request, f'Added {product.name} to your bag.')

    request.session['bag'] = bag        # Overwrites variable in session with updated version
    return redirect(redirect_url)


# --------------------------------------------------------- Adjust bag
def adjust_bag(request, item_id):
    """ Adjusts the quantity of specified product to specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))    # Needs conversion to int as comes as string from from
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})    # Keeps bag contents while session lasts. If not session, it creates one

    if size:                                            # If product has sizes...
        if quantity > 0:                                        # ... and if quantity is greater than 0...
            bag[item_id]['items_by_size'][size] = quantity      # ... sets quantity accordingly...
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}.')
        else:                                                   # ... otherwise...
            del bag[item_id]['items_by_size'][size]             # ... removes the item of that size
            if not bag[item_id]['items_by_size']:               # If there is no ohter sizes of the same item in bag...
                bag.pop(item_id)                                # ... removes item completely
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag.')
    else:                                               # If product does not have sizes...
        if quantity > 0:                                        # ... and if quantity is greater than 0...
            bag[item_id] = quantity                             # ... sets quantity accordingly...
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}.')
        else:                                                   # ... otherwise...
            bag.pop(item_id)                                    # ... removes the item completely
            messages.success(request, f'Removed {product.name} from your bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


# --------------------------------------------------------- Remove contents from bag
def remove_from_bag(request, item_id):
    """ Removes item from bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})    # Keeps bag contents while session lasts. If not session, it creates one

        if size:                                        # If product has sizes...
            del bag[item_id]['items_by_size'][size]         # ... removes the item of that size
            if not bag[item_id]['items_by_size']:           # If there is no ohter sizes of the same item in bag...
                bag.pop(item_id)                            # ... removes item completely
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag.')
        else:                                           # If product does not have sizes...
            bag.pop(item_id)                                # ... removes the item completely
            messages.success(request, f'Removed {product.name} from your bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
