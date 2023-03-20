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

# class ProductList(generics.ListCreateAPIView):
    # 
    # 
# 
# class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    # 
    # 
    # 
# class CollectionList(generics.RetrieveUpdateDestroyAPIView):
    # 
    # 
    # 
# class ShoppingList(generics.ListCreateAPIView):