from django.shortcuts import render


# --------------------------------------------------------- View Bag contents
def view_bag(request):
    """ Renders bag contents page """
    return render(request, 'bag/bag.html')
