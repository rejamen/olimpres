# Generated by Django 3.0.3 on 2020-05-24 00:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OlimpresStock', '0003_auto_20200523_2042'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='product',
            name='product_base_price_non_negative',
        ),
        migrations.AlterField(
            model_name='product',
            name='base_price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator('0.01')], verbose_name='Precio base'),
        ),
    ]