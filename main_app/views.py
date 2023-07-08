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