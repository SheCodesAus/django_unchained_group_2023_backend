from django.shortcuts import render
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


from rest_framework.views import APIView
from django.http import Http404

from .models import Product
from .serializers import ProductSerializer


# Create your views here.

""" Product Detail View """
""" There is no product list view because THESE ARE the COLLECTION DETAIL VIEWS! It's likely we don't even need this particular view and just require the serializer for the product, however including just incase."""

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ("price", "brand", "name",)

    