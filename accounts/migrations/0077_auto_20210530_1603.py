# Generated by Django 3.2 on 2021-05-30 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0076_auto_20210530_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='transaction_id',
        ),
    ]
