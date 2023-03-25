from django.db import models
# from .models import User 
# Collection

# Create your models here.

""" Product Model """


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image_url = models.URLField(blank=True, null=True)
    product_url = models.URLField(blank=True, null=True)
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    notes = models.TextField(max_length=500)
    collection = models.CharField(blank=True, null=True, max_length=200)
    user = models.ForeignKey(
        to="users.CustomUser",
        on_delete=models.CASCADE,
    )

    # class Meta:
    #     abstract = True


    # add_to_list = (models.BooleanFiled) cannot be a field on the product model because we are wanting the user to assign the product to a collection upon initial input of that product into the app. 

    # don't need related names for users because there is only 1 user in this app at all times.

    # created another app for products because collection model in shoppinglist app references products model due to the need for a foreign key for the product field, and the product model references collection model due to the need for a foreign key for the collection field. Placing either one above or below each other in the same model file would always cause a problem for one of the two, depending on which one was below. 

    # There is an issue here with having a collection field in product. This means that a collection must already exist for the user to register a product. This creates a 'chicken before the egg situation' - a never ending loop (as a collection states that a product is a required field). This needs to change.
    # Either the user must be able to add a product without being obligated to assign a collection to it, which will require a separate product serializer, view and url, and/or
    # a user must be able to create collections without stipulating a product.
    # Realistically, they should be able to do both.