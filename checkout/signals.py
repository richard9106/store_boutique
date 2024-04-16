from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import OrderLinItem


@receiver(post_save, sender=OrderLinItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update oder total on lineitem update/create
    """
    instance.order.update_total()
    

@receiver(post_delete, sender=OrderLinItem)
def delete_on_save(sender, instance, **kwargs):
    """
    update oder total on lineitem update/create
    """
    instance.order.update_total()