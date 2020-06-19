<<<<<<< HEAD
import uuid     # Used to generate the order number
=======
import uuid     # Used to generate order number
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


<<<<<<< HEAD
# --------------------------------------------------------- ORDER
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)  # Automatically generated and not editable
=======
# --------------------------------------------------------- Order
class Order(models.Model):
    """ Base for the order form """
    order_number = models.CharField(max_length=32, null=False, editable=False)  # Automatically generated
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
<<<<<<< HEAD
    date = models.DateTimeField(auto_now_add=True)  # Automatically sets order date and time
=======
    date = models.DateTimeField(auto_now_add=True)  # Automatically sets order date and time when order is placed
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

<<<<<<< HEAD
    # ------------------------------------------- Generate order number method
    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()     # Generates random string of 32 characters

    # ------------------------------------------- Update total method
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    # ------------------------------------------- Custom save method
=======
    def _generate_order_number(self):
        """
        Generates a random, unique string of 32 characters
        order unumber using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:  # If order total doesn't reach free delivery treshold...
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE /100 # ... calculate delivery cost
        else:                                                   # If it is above free delivery treshold...     
            self.delivery_cost = 0                              # ... set delivery cost to 0
        self.grand_total = self.order_total + self.delivery_cost    # Then calculate the grand total...
        self.save()                                                 # and save the instance

>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


<<<<<<< HEAD
# --------------------------------------------------------- ORDER LINE ITEM
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)    # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    # --------------------------------- Custom save method
=======
# --------------------------------------------------------- Order line item
class OrderLineItem(models.Model):
    """ Relates to specific order """
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
