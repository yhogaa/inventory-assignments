# Generated by Django 4.2.5 on 2023-09-26 17:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_item_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
