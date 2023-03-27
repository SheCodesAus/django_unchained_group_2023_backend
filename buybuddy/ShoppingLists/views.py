from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured

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
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CollectionSerializer(queryset, many=True, context={'request': request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No collection found'}, status=status.HTTP_404_NOT_FOUND)

class CollectionDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_object(self, pk):
        try:
            collection = Collection.objects.get(pk=pk)
            self.check_object_permissions(self.request, collection)
            return collection
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
        single_collection = Collection.objects.get(pk=pk)
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
    permission_classes = [permissions.IsAuthenticated]
  

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
    permission_classes = [permissions.IsAuthenticated]







