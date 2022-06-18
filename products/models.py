from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField('Product Name', max_length=100)
    sku = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    has_stick_size = models.BooleanField(default=False, null=True, blank=True)
    has_clothes_size = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField('Description')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True)
    image_url = models.URLField('Image URL', max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
