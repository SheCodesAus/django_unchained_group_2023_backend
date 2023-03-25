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
        model = Product   
        fields = '__all__'
    
    def create (self, validated_data):
        return Product.objects.create (**validated_data)
    
    # def update(self, instance, **kwargs):
    #     instance.save()
    #     return instance
    
    """ Ability to edit product use both def update and use RetrieveUpdateDestroyAPIView in view.py - is that correct? See notes from https://www.django-rest-framework.org/api-guide/serializers/"""    
class ProductDetailSerializer(ProductSerializer):
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image_url = validated_data.get('image_url',instance.image_url)
        instance.product_url = validated_data.get('product_url', instance.product_url)
        instance.price = validated_data.get('price', instance.price)
        instance.brand = validated_data.get('brand',instance.brand)
        instance.notes = validated_data.get('notes',instance.notes)
        instance.add_to_shoppinglist = validated_data.get('add_to_shoppinglist',instance.add_to_shoppinglist)
        instance.save()
        return instance
   

class CollectionSerializer(serializers.Serializer):
    """Many to many relationship: Collection and product_id"""
    product_id = ProductSerializer(many=True, read_only=True, source='collection_product_id')
    # product_id = serializers.ReadOnlyField(many=True, read_only=True, source='collection_product_id')
    
    class Meta:
        model = Collection
        fields = ('name', 'user', 'product_id')
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
        
    