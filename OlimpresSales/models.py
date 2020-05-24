from django.db import models

# Python imports
from datetime import datetime

# Django imports
from OlimpresPeople import models as people_models
from OlimpresStock import models as stock_models


class SaleOrder(models.Model):
    """Every order in Olimpres is a Sale Order."""

    code = models.CharField(
        max_length=15,
        editable=False,
    )
    partner_id = models.ForeignKey(
        people_models.Partner,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Cliente',
    )
    product_id = models.ForeignKey(
        stock_models.Product,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Producto',
    )

    class Meta:
        verbose_name_plural = 'Ventas'

    def __str__(self):
        """How this record will be displayed."""
        return self.code
    
    def save(self, *args, **kwargs):
        """Extend save method to create sale order code.
        
        It will follow the format SO/<year>/<0000 padding> ID
        e.g: SO/2020/000015
        """
        # TODO: check if exists another way to avoid 
        #  calling save method twice
        super().save(*args, **kwargs)
        self.code = 'SO/{}/{:0>6d}'. \
            format(datetime.today().year, self.id)
        super().save(*args, **kwargs)
    