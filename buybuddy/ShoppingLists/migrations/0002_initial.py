# Generated by Django 4.1.5 on 2023-03-25 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShoppingLists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='collection_product',
            field=models.ManyToManyField(null=True, related_name='product_item', to='products.product'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]