# Generated by Django 3.2 on 2021-05-30 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_remove_order_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]