from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Collection, ShoppingList
from .serializers import CollectionSerializer, ShoppingListSerializer
# from products.models import Products
# from products.serializers import ProductSerializer



""" Collection List View """
""" A more specific version of a 'product list view """


class CollectionList(generics.RetrieveDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]
    lookup_field = 'pk'


    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, pk):
        serializer = CollectionSerializer(data=request.pk)
        if serializer.is_valid():
            try:
                serializer.save(owner=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(
                    {"error": "A collection with this name already exists. Please choose another name."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    # def post(self):
    #     serializer = CollectionSerializer()
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    

    # def get(self):
    #     collection = Collection.objects.all()
    #     serializer = CollectionSerializer()
    #     return Response(serializer.data)
    
    # def delete(self, pk):
    #     collection = self.get_object(pk=pk)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def perform_create(self, serializer):
    #     serializer.save

""" Collection Detail View """


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer




    # def get_object(self, pk):
    #     try:
    #         collection = Collection.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, collection)
    #         return collection
    #     except Collection.DoesNotExist:
    #         raise Http404
        
    # def get(self, request, pk):
    #     collection = self.get_object(pk=pk)
    #     serializer = CollectionSerializer(collection)
    #     return Response(serializer.data)


""" Shopping List View """

class ShoppingList(generics.RetrieveUpdateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def perform_create(self, serializer):
        serializer.save()
