# Generated by Django 3.0.8 on 2020-08-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20200818_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stripe_receipt',
            field=models.URLField(blank=True, default='', max_length=254),
        ),
    ]
