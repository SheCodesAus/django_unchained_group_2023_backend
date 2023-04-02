from rest_framework import serializers
from .models import Collection, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class ProductDetailSerializer(ProductSerializer):
    def update(self, instance, validated_data):
        instance.product_brand = validated_data.get('product_brand', instance.product_brand)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.product_url = validated_data.get('product_url', instance.product_url)
        instance.product_price = validated_data.get('product_price', instance.product_price)
        instance.additional_notes = validated_data.get('additional_notes', instance.additional_notes)
        instance.collection = validated_data.get('collection', instance.collection)
        return instance
  


class CollectionSerializer(serializers.ModelSerializer):
    collection_name = serializers.CharField()
    product_collection = ProductSerializer(many=True, read_only=True)


    class Meta:
        model = Collection
        fields = "__all__"
        # exclude = ['id']













