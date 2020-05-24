from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """Every service in Olimpres is a Product.

    """

    name = models.CharField(max_length=100)
    base_price = models.FloatField(
        verbose_name='Precio base',
        validators=[MinValueValidator(0.0)]
    )

    class Meta:
        verbose_name_plural = 'Productos'


    def __str__(self):
        """How this record will be displayed."""
        return self.name
