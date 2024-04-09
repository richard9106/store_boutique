from django.db import models


# Create your models here.
class Category(models.Model):
    """Info of the diferent categories for our products"""

    class Meta:
        """select a name to display in admin"""
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        """returne the name"""
        return self.name

    def get_friendly_name(self):
        """get firendly name"""
        return self.friendly_name


class Product(models.Model):
    """model for products"""
    category =  models.ForeignKey("Category", 
                                  null=True, 
                                  blank=True, 
                                  on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name