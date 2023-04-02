from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from .permissions import IsOwner
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer, ProductDetailSerializer


class CollectionListCreateView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def list(self, request, *args, **kwargs):
        # queryset = self.get_queryset()
        queryset = Collection.objects.all().filter(owner=self.request.user)

        serializer = CollectionSerializer(queryset, many=True, context={'request': request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No collection found'}, status=status.HTTP_404_NOT_FOUND)

class CollectionDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_object(self, request, pk):
        try:
            collection = Collection.objects.get(pk=pk)
            self.check_object_permissions(self.request, collection)
            return collection.objects.filter(owner=self.request.user)
        except Collection.DoesNotExist:
            raise Http404

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer()
    #     if instance:
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response({'Message': 'No collection found'}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        single_collection = self.get_object(pk, request)
        serializers = CollectionSerializer(single_collection)
        return Response(serializers.data)
    
    def put(self, request, pk):
        collection = self.get_object(pk)
        data = request.data
        serializer = CollectionSerializer(
            instance=collection,
            data=data,
            partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        collection = self.get_object(pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
  

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message':'No products found'}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]




# Nirali's link: https://stackoverflow.com/questions/54772183/django-rest-framework-permissions-and-ownership?fbclid=IwAR0JOcO5miec3hDQ8jFFIHplPPUMPRag7zJRrSqrTA3Xmj78UBXl6uVXJa4

# Laura's link
# https://stackoverflow.com/questions/34860988/django-rest-framework-restricting-user-access-for-objects 


# def get_queryset(self): return Book.objects.filter(user=self.request.user) 

# object permissions as opposed to model permissions? - Bridgitte

# https://www.geeksforgeeks.org/customizing-object-level-permissions-django-rest-framework/
# making a customised class?


# Error message: Field 'id' expected a number but got <rest_framework.request.Request: GET '/collection-detail/1/'>.
# This comes up when a user tries to view their own collection detail view.

# Error message: 'Product' object has no attribute 'owner'
# product needs an owner to post now?



# {
#     "product_brand": "Breville",
#     "product_name": "NUTRIBULLET XXL Digital Air Fryer",
#     "image_url": "https://thegoodguys.sirv.com/products/50076813/50076813_778587.PNG?scale.height=505&scale.width=773&canvas.height=505&canvas.width=773&canvas.opacity=0&q=90",
#     "product_url": "https://www.thegoodguys.com.au/nutribullet-xxl-digital-air-fryer-nba07100",
#     "product_price": 299,
#     "additional_notes": "black",
#     "collection": 2
# }

