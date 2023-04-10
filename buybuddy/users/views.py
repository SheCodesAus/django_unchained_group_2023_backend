from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsLoggedIn

class CustomUserList(APIView):
    
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
class CustomUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
            
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

class AuthenticatedUser(APIView):
    def get_object(self):
        try:
            return self.request.user
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, request):
        user = self.get_object()
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
class Shoppinglist(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
            
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def post(self, request, pk):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors)
        
# class Shoppinglist(generics.ListCreateAPIView):
#     serializer_class = CustomUserSerializer
#     def get_queryset(self):
#         pk = self.kwargs["pk"]
#         return CustomUser.objects.get(pk=pk).my_favorites.all()
    
#     def create(self, request, *args, **kwargs):
#         qs = self.get_queryset()
#         pk = self.kwargs["pk"]
#         user = CustomUser.objects.get(pk=pk)
#         if qs.filter(id=self.request.user.id).exists():
#             user.my_favorites.remove(self.request.user)
#         else: 
#             user.my_favorites.add(self.request.user)
#         serializer = self.get_serializer(user.my_favorites.all(), many=True)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)