from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Collection, ShoppingList
from .serializers import ProductSerializer, CollectionSerializer, ShoppingListSerializer
#import permissions as well

# Create your views here, expand them

class CollectionList(generics.ListAPIView):
    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self, pk):
        try:
            collection = Collection.objects.get(pk=pk)
            self.check_object_permissions(self.request, collection)
            return collection
        except Collection.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        collection = self.get_object(pk=pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)



# class ProductList(generics.ListAPIView):

#     def get_object(self, pk):
#         try:
#             product = Product.objects.get(pk=pk)
#             self.check_object_permissions(self.request, product)
#             return product
#         except Product.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
    
    

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingList(generics.RetrieveUpdateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
