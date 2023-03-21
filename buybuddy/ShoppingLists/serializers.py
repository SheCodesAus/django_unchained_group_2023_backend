from rest_framework import serializers
from .models import Product, Collection, ShoppingList

class ProductSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    # name = serializers.CharField(max_length=200)
    # image_url = serializers.URLField()
    # product_url = serializers.URLField()
    # price = serializers.IntergerField()
    # brand = serializers.CharField(max_length=100)
    # notes = serializers.CharField(max_length=500)
    # add_to_shoppinglist = serializers.BooleanField()
    # user = serializers.ReadOnlyField (source="user_product")
    
    class Meta:
        fields = ('id', 'name', 'image_url', 'product_url', 'price', 'brand', 'notes', 'add_to_shoppinglist')
        model = Product   
    
    def create (self, validated_data):
        return Product.objects.create (**validated_data)
    
    """ Ability to edit product use both def update and use RetrieveUpdateDestroyAPIView in view.py - is that correct? See notes from https://www.django-rest-framework.org/api-guide/serializers/"""    
   
   

class CollectionSerializer(serializers.ModelSerializer):
    """Many to many relationship: Collection and product_id"""
    product_id = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Collection
        fields = ('id', 'name')
        read_only_fields = ('product_id', 'user_id')
        
    def create(self, validated_data):
        return Collection.objects.create(**validated_data)   
    
          
        
class ShoppingListSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = ShoppingList
        fields = ('total_cost')
        read_only_fields = ('product_id', 'user_id')
              
    def create (self, validated_data):
        return ShoppingList.objects.create (**validated_data)
    
    """Do we need @property to calculate total?"""
        
    