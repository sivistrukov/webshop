# Generated by Django 4.1.3 on 2022-11-10 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
