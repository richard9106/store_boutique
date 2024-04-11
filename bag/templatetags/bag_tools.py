"""import templates"""
from django import template

register = template.Library()

@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    """calculated the subtotal"""
    return price * quantity

