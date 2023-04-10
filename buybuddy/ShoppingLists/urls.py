from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("collection-list/", views.CollectionListCreateView.as_view(), name='collection-list'),
    path("collection-detail/<int:pk>/", views.CollectionDetailView.as_view(), name='collection-detail'),
    path("product-list/", views.ProductListCreateView.as_view(), name='product-list'),
    path("product-detail/<int:pk>/", views.ProductDetailView.as_view(), name='product-detail'),
    path("favourites/", views.FavouriteList.as_view(), name='product-favourite'),


]

