# Generated by Django 4.1.5 on 2023-04-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingLists', '0007_remove_product_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
