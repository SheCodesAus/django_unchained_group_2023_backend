# Generated by Django 4.1.5 on 2023-04-04 10:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShoppingLists', '0004_product_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='favorite',
        ),
        migrations.AddField(
            model_name='product',
            name='favorite',
            field=models.ManyToManyField(related_name='shoppinglist_product', to=settings.AUTH_USER_MODEL),
        ),
    ]
