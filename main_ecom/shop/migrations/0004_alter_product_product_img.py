# Generated by Django 5.0.7 on 2024-08-28 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='', upload_to='media/shop/images'),
        ),
    ]
