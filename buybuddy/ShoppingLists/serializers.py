from rest_framework import serializers
from .models import Collection, ShoppingList
from products.models import Product
from products.serializers import ProductSerializer

""" UN-NESTED APPROACH - THIS DID NOT WORK"""


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



""" NESTED APPROACH USING HYPERLINKEDMODELSERIALIZER - IF SHIT HITS THE FAN! NOT ATTEMPTED"""

# class CollectionSerializer(serializers.HyperlinkedModelSerializer):
#     product = ProductSerializer(many=True)

#     class Meta:
#         model = Collection
#         fields = ['name', 'product']




""" NESTED APPROACH WITH DEPTH SPECIFIED"""

# https://www.django-rest-framework.org/api-guide/relations/#nested-relationships

# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

class CollectionSerializer(serializers.ModelSerializer):
    """Many to many relationship: Collection and product"""
    product = ProductSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Collection
        depth = 3
        fields = ['name', 'product'] 

    def update(self, instance, validated_data):
        product_data = validated_data.pop('product')
        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        product = instance.product
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        product.image_url = product_data.get('image_url', product.image.url)
        product.save()
        product.price = product_data.get('price', product.price)
        product.save()
        product.brand = product_data.get('brand', product.brand)
        product.save()
        product.notes = product_data.get('notes', product.notes)
        product.save()   
        product.collection = product_data.get('collection', product.collection)
        product.save()     
        product.save()
        return instance

class CollectionDetailSerializer(CollectionSerializer):
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='name', many=True, required=False)
    class Meta:
        model = Collection
        depth = 2
        fields = ['name', 'product'] 

    def update(self, instance, validated_data):
        product_data = validated_data.pop('product')
        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        product = instance.product
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        product.image_url = product_data.get('image_url', product.image.url)
        product.save()
        product.price = product_data.get('price', product.price)
        product.save()
        product.brand = product_data.get('brand', product.brand)
        product.save()
        product.notes = product_data.get('notes', product.notes)
        product.save()   
        product.collection = product_data.get('collection', product.collection)
        product.save()     
        product.save()

        name= instance.name
        name.save()

        return instance

# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
# nested serializers are read-only. If you want to support write-operations to a nested serializer field one must include create() and/or update() methods in order to explicitly specify how the child relationships should be saved.

    # def create(self, validated_data):
    #     product_data = validated_data.pop('product')
    #     collection = Collection.objects.create(**validated_data)
    #     for product_data in product_data:
    #         Product.objects.create(collection=collection, **product_data, 
    #     )
    #     Collection.save()
    #     return Collection


# https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments

    # def post(self, validated_data):
    #     collection = Collection(
    #         name=validated_data['name'],
    #         product_data = validated_data.pop('product'),
    #         user_data = validated_data.pop('user')),
    #     collection = Collection.objects.create(**validated_data)
    #     collection.save()
    #     return Collection    








class ShoppingListSerializer(serializers.ModelSerializer):
    product = CollectionSerializer(many=True)    
    class Meta:
        model = ShoppingList
        fields = ['total_cost']
        depth = 2

    def update(self, instance, validated_data):
        product_data = validated_data.pop('product')
        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        product = instance.product
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        product.image_url = product_data.get('image_url', product.image.url)
        product.save()
        product.price = product_data.get('price', product.price)
        product.save()
        product.brand = product_data.get('brand', product.brand)
        product.save()
        product.notes = product_data.get('notes', product.notes)
        product.save()   
        product.collection = product_data.get('collection', product.collection)
        product.save()
        product.save()
        return instance

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        shopping_list = ShoppingList.objects.create(**validated_data)
        for product_data in product_data:
            Product.objects.create(shopping_list=shopping_list, **product_data, 
        )
        ShoppingList.save()
        return ShoppingList
    

