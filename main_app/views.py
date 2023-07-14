from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .serializers import NFTSerializer, UserSerializer
from .models import NFT

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class NFTViewSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [permissions.IsAdminUser]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Login Successful"})
        else:
            return Response({"detail": "Invalid credentials"})
        

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({"detail": "Logout Successful"})

class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('email')  # Use email as username
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('firstName')
        last_name = request.data.get('lastName')
        ethereum_address = request.data.get('ethereumAddress')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'A user with this email already exists'}, status=400)

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Save the Ethereum address in the user's profile
        user.profile.ethereum_address = ethereum_address
        user.profile.save()
        

        return Response({'message': 'User created successfully'}, status=201)
