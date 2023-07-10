from rest_framework import viewsets, permissions

from .serializers import NFTSerializer, UserSerializer
from .models import NFT
from django.contrib.auth.models import User

# Create your views here.
class NFTViewSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [permissions.IsAdminUser]

# views.py

from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Login Successful"})
        else:
            return Response({"detail": "Invalid credentials"})
