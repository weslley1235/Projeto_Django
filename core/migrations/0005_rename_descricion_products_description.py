# Generated by Django 5.0.7 on 2024-07-24 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_products_descricion_products_pro_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='descricion',
            new_name='description',
        ),
    ]
