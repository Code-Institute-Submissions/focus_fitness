# Generated by Django 3.0.8 on 2020-08-24 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_sale_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sale_price',
            new_name='was_price',
        ),
    ]
