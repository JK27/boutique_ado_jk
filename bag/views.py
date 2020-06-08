from django.shortcuts import render, redirect


# --------------------------------------------------------- View Bag contents
def view_bag(request):
    """ Renders bag contents page """
    return render(request, 'bag/bag.html')


# --------------------------------------------------------- Add contents to bag
def add_to_bag(request, item_id):
    """ Adds quantity of specified product to shopping bag """

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
            else:                                                   # ... but if it has a different size...
                bag[item_id]['items_by_size'][size] = quantity      # ... then add quantity of items of that size
        else:                                                       # But if product is not already in bag...
            bag[item_id] = {'items_by_size': {size: quantity}}      # ... adds quantity of items of each size to bag
    else:                                   # If product does not have sizes...
        if item_id in list(bag.keys()):     # ...and if item already exists in bag ...
            bag[item_id] += quantity        # ...updates quantity accordingly
        else:                               # But if item not alreay in bag ...
            bag[item_id] = quantity         # ... adds specified quantity of items to bag

    request.session['bag'] = bag        # Overwrites variable in session with updated version
    return redirect(redirect_url)
