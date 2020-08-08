# Generated by Django 3.0.8 on 2020-08-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]