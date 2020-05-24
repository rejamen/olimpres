# Generated by Django 3.0.3 on 2020-05-24 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OlimpresStock', '0001_initial'),
        ('OlimpresPeople', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(editable=False, max_length=15)),
                ('partner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OlimpresPeople.Partner', verbose_name='Cliente')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OlimpresStock.Product', verbose_name='Producto')),
            ],
            options={
                'verbose_name_plural': 'Ventas',
            },
        ),
    ]
