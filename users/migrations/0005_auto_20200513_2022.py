# Generated by Django 2.2.12 on 2020-05-13 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_address_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='location',
        ),
        migrations.RemoveField(
            model_name='deliveryman',
            name='location',
        ),
    ]
