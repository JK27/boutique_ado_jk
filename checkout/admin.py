from django.contrib import admin
from .models import Order, OrderLineItem


<<<<<<< HEAD
# --------------------------------------------------------- ORDER LINE ITEM
class OrderLineItemAdminInline(admin.TabularInline):
    """
    Allows to add and edit line items in admin from inside order model
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)   # Item total price is uneditable


# --------------------------------------------------------- ORDER ADMIN
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    # --- Fields calculated automatically by models
=======
# --------------------------------------------------------- Order Lineitem
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


# --------------------------------------------------------- Order
class OrderAdmin(admin.ModelAdmin):
    """
    Not editable fields as they are calculated by model methods.
    """
    inlines = (OrderLineItemAdminInline,)

>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

<<<<<<< HEAD
    # --- Specifies order of fields to match model
=======
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

<<<<<<< HEAD
    # --- Restricts columns showing up in order list
=======
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

<<<<<<< HEAD
    # --- Order in reverse chronological order with most recent at top
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
=======
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
