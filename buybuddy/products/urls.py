from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
