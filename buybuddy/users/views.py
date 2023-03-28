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