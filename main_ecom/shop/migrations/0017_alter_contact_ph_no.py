# Generated by Django 5.0.7 on 2024-08-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ph_no',
            field=models.IntegerField(null=True),
        ),
    ]