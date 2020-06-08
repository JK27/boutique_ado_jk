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
    bag = request.session.get('bag', {})    # Keeps bag contents while session lasts. If not session, it creates one

    if item_id in list(bag.keys()):     # If item already exists in bag ...
        bag[item_id] += quantity        # ...updates quantity accordingly
    else:                               # If item not alreay in bag ...
        bag[item_id] = quantity         # ... adds specified quantity of items to bag

    request.session['bag'] = bag        # Overwrites variable in session with updated version
    return redirect(redirect_url)
