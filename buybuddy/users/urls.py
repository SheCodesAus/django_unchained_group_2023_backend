from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CustomUserList.as_view(), name='customuser-list'),
    path('<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
    path('<int:pk>/change_password/', views.ChangePasswordView.as_view(), name='auth_change_password')
]

urlpatterns = format_suffix_patterns(urlpatterns)