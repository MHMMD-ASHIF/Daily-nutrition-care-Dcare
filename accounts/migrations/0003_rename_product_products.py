# Generated by Django 3.2 on 2021-04-17 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product',
            new_name='products',
        ),
    ]
