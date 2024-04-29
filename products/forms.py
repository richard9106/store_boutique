from django import forms
from .models import Product, Category


class ProductForms(forms.ModelForm):
    """ Form to load products to the store"""

    class Meta:
        model = Product
        field = '__all__'

    def __init__(self, *args, **kwargs):
        """ Init methood"""
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.field['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-0 rounded-0'