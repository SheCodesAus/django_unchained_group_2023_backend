from rest_framework import serializers
from .models import Product
from ShoppingLists.models import Collection
# from ShoppingLists.serializers import CollectionSerializer

class ProductSerializer(serializers.ModelSerializer):
    # collection = CollectionSerializer(many=True, required=False)
    
    # collection = serializers.SlugRelatedField(queryset=Collection.objects.all(), slug_field="name",
    #     many=True)

    class Meta:
        model = Product   
        fields = ['name', 'image_url', 'product_url', 'price', 'brand', 'notes', 'collection']
        read_only_fields = ['id']
    
        def create(self, validated_data):
            return Product.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.image_url = validated_data.get('image_url', instance.image_url)
            instance.product_url = validated_data.get('product_url', instance.product_url)
            instance.price = validated_data.get('price', instance.price)
            instance.brand = validated_data.get('brand', instance.brand)
            instance.notes = validated_data.get('notes', instance.notes)
            instance.collection = validated_data.get('collection', instance.collection)
            instance.save()
            return instance

        def get(self, instance):
            return instance

    
    """ Ability to edit product use both def update and use RetrieveUpdateDestroyAPIView in view.py - is that correct? See notes from https://www.django-rest-framework.org/api-guide/serializers/"""    
