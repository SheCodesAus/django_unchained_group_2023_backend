from rest_framework import serializers
from .models import Collection, Product
from users.models import CustomUser
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = "__all__"
        exclude = ['owner']

class ProductDetailSerializer(ProductSerializer):
    image_upload = serializers.ImageField(required=False)

    class Meta:
        model = Product
        exclude = ['owner']

    def update(self, instance, validated_data):
        instance.product_brand = validated_data.get('product_brand', instance.product_brand)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.image_upload = validated_data.get('image_upload', instance.image_upload)
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
        # fields = "__all__"
        exclude = ['owner']



# For CollectionSerializer to only show the authenticated user's collections as options when adding a product to a collection;
# override the __init__ method of the serializer to take the request object as a keyword argument. Call the superclass __init__ method with the remaining arguments, which initializes the serializer as usual. Check if the request object is present and the user is authenticated. If both conditions are met, update the owner field to only show the authenticated user as an option by setting the queryset to CustomUser.objects.filter(pk=request.user.pk) and setting the default value to request.user.

# Override create method to set the owner to the authenticated user, and the update method to remove the owner field from the validated data before calling the superclass update method.


    # def __init__(self, *args, **kwargs):
    #     request = kwargs.pop('request', None)
    #     super(CollectionSerializer, self).__init__(*args, **kwargs)

    #     if request and request.user.is_authenticated:
    #         self.fields['owner'].queryset = CustomUser.objects.filter(pk=request.user.pk)
    #         self.fields['owner'].default = request.user

    # def create(self, validated_data):
    #     validated_data['owner'] = self.context['request'].user
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     validated_data.pop('owner', None)
    #     return super().update(instance, validated_data) 



    # THIS METHOD DID NOT WORK; 
    # only show the authenticated user's collections as options when adding a product to a collection;
    # Validate_product_collection method receives the list of collections as value. It then retrieves the authenticated user from the context (in views)and filters the collections to only show those that belong to the use
    # def validate_product_collection(self, value):
    #     # Get the authenticated user
    #     user = self.context['request'].user

    #     # Filter out collections that don't belong to the authenticated user
    #     filtered_collections = value.filter(owner=user)

    #     return filtered_collections










