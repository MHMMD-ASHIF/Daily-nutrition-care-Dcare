# Generated by Django 3.2 on 2021-05-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20210525_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='first_name',
            new_name='aboutme',
        ),
        migrations.AddField(
            model_name='users',
            name='firstname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]