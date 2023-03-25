from rest_framework import serializers
from .models import Collection, ShoppingList
from products.models import Product
from products.serializers import ProductSerializer

""" UN-NESTED APPROACH """
# class CollectionSerializer(serializers.ModelSerializer):
#     """Many to many relationship: Collection and product"""
    
#     product = ProductSerializer(many=True, read_only=True, source='product')
    
#     class Meta:
#         model = Collection
#         fields = ('name', 'user', 'product')
#         read_only_fields = ('product', 'user')
        
#     def create(self, validated_data):
#         return Collection.objects.create(**validated_data)   
    
        
# class ShoppingListSerializer(serializers.ModelSerializer):
    
#     product = CollectionSerializer(many=True, read_only=True, source='product')
#     class Meta: 
#         model = ShoppingList
#         fields = ['total_cost']
#         read_only_fields = ['product', 'user']
              
#     def create (self, validated_data):
#         return ShoppingList.objects.create (**validated_data)
    
#     """Do we need @property to calculate total?"""
        

""" NESTED APPROACH"""




class CollectionSerializer(serializers.ModelSerializer):
    """Many to many relationship: Collection and product"""
    
    product = ProductSerializer(many=True)
    # products = ProductSerializer(many=True)

    class Meta:
        model = Collection
        fields = ('name', 'user', 'product')
        read_only_fields = ('user')

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        collection = Collection.objects.create(**validated_data)
        for product_data in product_data:
            Product.objects.create(product=product, **product_data)
        return product

class ShoppingListSerializer(serializers.ModelSerializer):
    
    product = CollectionSerializer(many=True)
    
    class Meta:
        model = ShoppingList
        fields = ['total_cost']
        read_only_fields = ['product', 'user']
