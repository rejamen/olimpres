# Generated by Django 3.0.3 on 2020-05-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OlimpresStock', '0002_product_base_price'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='product',
            constraint=models.CheckConstraint(check=models.Q(base_price__gte='0'), name='product_base_price_non_negative'),
        ),
    ]
