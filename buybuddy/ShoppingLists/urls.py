from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('collections/', views.CollectionList.as_view(), name='collections'),
    path('collections/<int:pk>', views.CollectionDetail.as_view(), name='collection-detail'),
    path('shoppinglists/', views.ShoppingList.as_view(), name='shoppinglists'),

]

urlpatterns = format_suffix_patterns(urlpatterns)