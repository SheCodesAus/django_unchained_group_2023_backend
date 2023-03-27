from django.shortcuts import render
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


from rest_framework.views import APIView
from django.http import Http404

from .models import Product
from .serializers import ProductSerializer


# Create your views here.

""" Product List View """

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [filters.SearchFilter]
    # filterset_fields = ("price", "brand", "name",)


""" Product Detail View"""
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [filters.SearchFilter]
    # filterset_fields = ("price", "brand", "name",)

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response(
                {"data": "The product you are looking for does not exist."}, status=status.HTTP_404_NOT_FOUND
            )
        return super(ProductDetail, self).handle_exception(exc)
    