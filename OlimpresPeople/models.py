from django.db import models
from django.core.validators import EmailValidator


class Partner(models.Model):
    """Every person in Olimpres is a Partner."""

    name = models.CharField(max_length=100)
    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        validators=[EmailValidator]
    )
    mobile = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Móvil',
        help_text='Móvil de contacto'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Teléfono',
        help_text='Teléfono de contacto'
    )
    address1 = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Calle/No.',
    )
    address2 = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Entre calles/Rpto/otros',
    )
    city_id = models.ForeignKey(
        'City',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Ciudad',
    )

    def __str__(self):
        """How this record will be displayed."""
        return self.name

    def get_full_address(self):
        """Get full address for this partner."""
        return '{} {} \n {}'.format(self.address1, self.address2, self.city_id.name)


class City(models.Model):
    """City model for Olimpres."""

    name = models.CharField(
        max_length=100,
        verbose_name='Nombre',
    )

    class Meta:
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        """How this record will be displayed."""
        return self.name
