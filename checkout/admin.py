from django.contrib import admin
from .models import Order, OrderLinItem
# Register your models here.


class OrderLineItemAdmin(admin.TabularInline):
    """display a list of the editable line items in the same
    page so we don't have to go to inlineitem seccion admin"""
    model = OrderLinItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """Register the models to the admin"""
    inlines = (OrderLineItemAdmin,)

    readonly_fields = ('order_number',
                       'date',
                       'delivery_cost',
                       'order_total',
                       'grand_total',)

    fields = ('order_number',
              'date',
              'full_name',
              'email',
              'phone_number',
              'country',
              'post_code',
              'town_or_city',
              'street_address1',
              'street_address2',
              'county',
              'delivery_cost',
              'order_total',
              'grand_total',
              )

    list_display = ('order_number',
                    'date',
                    'full_name',
                    'order_total',
                    'delivery_cost',
                    'grand_total',
                    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)