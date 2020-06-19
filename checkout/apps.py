from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

<<<<<<< HEAD
    """
    Overrides the ready method and imports custom signals module.
    Every time a line item is saved or deleted,
    custom update total model method will be called
    """
=======
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
    def ready(self):
        import checkout.signals
