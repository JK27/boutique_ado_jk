from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
<<<<<<< HEAD
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
=======
    path('checkout_success/<order_number>', views.checkout_success,
         name='checkout_success'),
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
]
