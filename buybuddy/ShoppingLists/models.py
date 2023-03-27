from django.db import models
from django.contrib.auth import get_user_model
# from .models import Product - this caused circular import error.

User = get_user_model()


""" Collection Model """

class Collection(models.Model):

    # pass

    name = models.CharField(unique=True, max_length=200,
                            null=False, blank=False)
    product = models.ManyToManyField(
        to="products.Product",
        related_name="product_item", blank=True
    )
    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE
    # )
    




""" Shopping List Model """


class ShoppingList(models.Model):

    # pass 

    product = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='favorite_item', null=True
    )
    total_cost = models.IntegerField()
    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE
    # )

@property
def final_cost(self):
    total_cost_sum = self.total_costs.aggregate(
        sum=models.Sum("total_cost"))["sum"]
    if total_cost_sum == None:
        return 0
    else:
        return total_cost_sum