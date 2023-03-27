from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured

from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Collection, ShoppingList
from .serializers import CollectionSerializer, CollectionDetailSerializer, ShoppingListSerializer
# from products.models import Products
# from products.serializers import ProductSerializer



""" Collection List View """
""" Technically a more specific version of a 'product list view """


class CollectionList(generics.ListCreateAPIView):
# this class does not work using generics.RetrieveUpdateDestroyAPIView, which is nice if we want to delete a collection without going into it. 
# Error message says; Expected view CollectionList to be called with a URL keyword argument named "pk". Fix your URL conf, or set the `.lookup_field` attribute on the view correctly.



    # Optimizing the query set, which contains a many-many (potentially performance hindering) field, using prefetch_related and passing that field.
    queryset = Collection.objects.all().prefetch_related('product')
    # get_queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["name"]
    # lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save()





""" Collection Detail View """


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Collection.objects.all()
    serializer_class = CollectionDetailSerializer


# https://www.fullstackpython.com/django-core-exceptions-improperlyconfigured-examples.html
    def get_queryset(self):
        if self.queryset is None:
            if self.model:
                return self.model._default_manager.all()
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        return self.queryset.all()

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response(
                {"data": "The collection you are looking for does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        return super(CollectionDetail, self).handle_exception(exc)




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





# For more complex cases may need to override various methods on the view class...
# https://www.django-rest-framework.org/api-guide/generic-views/

    # def get(self):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = CollectionSerializer(queryset, many=True, partial=True)
    #     # obj = queryset.get(pk=self)
    #     return Response(serializer.data)



    # def post(self, pk):
    #     serializer = CollectionSerializer(data=pk)
    #     if serializer.is_valid():
    #         try:
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         except IntegrityError:
    #             return Response(
    #                 {"error": "A collection with this name already exists. Please choose another name."},
    #                 status=status.HTTP_400_BAD_REQUEST,
    #             )
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    # def post(self, pk):
    #     serializer = CollectionSerializer(data=pk)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)
    

    # def get(self, data=CollectionSerializer):
    #     collection = Collection.objects.all()
    #     serializer = CollectionSerializer()
    #     return Response(serializer.data)
    
    # def delete(self, pk):
    #     collection = self.get_object(pk=pk)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)




""" Shopping List View """

class ShoppingList(generics.RetrieveUpdateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def perform_create(self, serializer):
        serializer.save()
