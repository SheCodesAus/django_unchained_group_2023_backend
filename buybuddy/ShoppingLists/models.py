from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

""" Product Model """


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image_url = models.URLField(blank=True, null=True)
    product_url = models.URLField(blank=True, null=True)
    price = models.IntegerField(decimal_places=2, max_digits=10)
    brand = models.CharField(max_length=100)
    notes = models.TextField(max_length=500)
    add_to_shoppinglist = models.BooleanField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_product'
    )


""" Collection Model """


class Collection(models.Model):
    name = models.CharField(unique=True, max_length=200,
                            null=False, blank=False)
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='collection_product_id'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_collection'
    )


""" Shopping List Model """


class ShoppingList(models.Model):
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='shoppinglist_product_id'
    )
    total_cost = models.IntegerField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_shoppinglist'
    )
