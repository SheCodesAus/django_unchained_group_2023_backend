# Generated by Django 4.1.5 on 2023-03-26 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingLists', '0003_rename_collection_product_collection_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='user',
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_item', to='ShoppingLists.collection'),
        ),
    ]