# Generated by Django 3.0.3 on 2020-05-24 00:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OlimpresPeople', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, validators=[django.core.validators.EmailValidator]),
        ),
    ]
