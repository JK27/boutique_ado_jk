from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


<<<<<<< HEAD
# --------------------------------------------------------- UPDATE ON SAVE
=======
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


<<<<<<< HEAD
# --------------------------------------------------------- UPDATE ON DELETE
=======
>>>>>>> ee7f4c3470de66cdc4030780d4e1b9601afd9a70
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
