# Generated by Django 5.0.7 on 2024-08-29 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_order_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order_details',
        ),
    ]
