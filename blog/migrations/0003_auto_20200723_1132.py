# Generated by Django 3.0.8 on 2020-07-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_category_friendly_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(default='cats', max_length=100),
        ),
    ]
