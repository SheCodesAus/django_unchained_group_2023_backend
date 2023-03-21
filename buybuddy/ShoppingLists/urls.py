from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.CollectionList.as_view(), name='collections'),
    path('collections/<int:pk>', views.CollectionDetail.as_view(), name='collection-detail'),
    path('shopping-list/', views.ShoppingList.as_view(), name='shopping-list'),
    

]