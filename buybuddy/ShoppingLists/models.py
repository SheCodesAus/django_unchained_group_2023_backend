from django.db import models
from django.contrib.auth import get_user_model




class Collection(models.Model):
    collection_name = models.CharField(max_length=250)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_collection')


    def __str__(self):
        return self.collection_name
    
    
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
    
class Product(models.Model):
    product_brand = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250)
    image_url = models.URLField(null=True)
    image_upload = models.ImageField(upload_to=upload_to, blank=True, null=True)
    product_url = models.URLField()
    product_price = models.FloatField()
    additional_notes = models.CharField(max_length=1000)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='product_collection')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_product')

    def __str__(self):
        return self.product_name
    
    