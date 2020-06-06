from django.shortcuts import render


# --------------------------------------------------------- Index view
def index(request):
    return render(request, 'home/index.html')
