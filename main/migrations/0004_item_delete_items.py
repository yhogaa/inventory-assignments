# Generated by Django 4.2.5 on 2023-09-13 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_items_category_alter_items_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('category', models.CharField(max_length=256)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]
