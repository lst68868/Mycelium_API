from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import NFTSerializer, UserSerializer
from .models import NFT
from django.http import JsonResponse
from django.views import View

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
    queryset = NFT.objects.all().order_by('-date_created')
    serializer_class = NFTSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class NFTTrendingSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all().order_by('-views')[:10]
    serializer_class = NFTSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class NFTDetailView(View):
    def get(self, request, *args, **kwargs):
        try:
            nft = NFT.objects.get(tokenId=self.kwargs['tokenId'])

            # Increment the views by 1
            nft.views += 1

            # Save the NFT instance
            nft.save()

            data = {
                'title': nft.title,
                'creator': nft.creator,
                'date_created': nft.date_created.isoformat(),
                'image_link': nft.image_link,
                'owned_by': nft.owned_by,
                'category': nft.category,
                'views': nft.views,
                'tokenId': nft.tokenId,
            }
            return JsonResponse(data)
        except NFT.DoesNotExist:
            return JsonResponse({'error': 'NFT not found'}, status=404)

    

    
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
        ethereum_address = request.data.get('ethereumAddress')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'A user with this email already exists'}, status=400)

        user = User.objects.create_user(username, email, password)
        user.save()

        # Save the Ethereum address in the user's profile
        profile = user.profile
        profile.ethereum_address = ethereum_address
        profile.save()

        return Response({'message': 'User created successfully'}, status=201)


class CreateNFTView(APIView):
    
    def post(self, request):
        print(request.data)
        serializer = NFTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class UserProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        # Fetch the user profile information or perform any other necessary operations
        profile_data = {
            'ethereum_address': user.profile.ethereum_address,
        }
        return Response(profile_data)
    
        """
        
            - Get User model to accept ethereum address *
            - Have address given in signup send to database *
            - Create an NFT with a new user.
            - Make sure the created NFT has the proper owned_by and other fields
            - Create an NFT and then go to nftinfo for it
            - Fix hard coded eth wallet in mintNFT function
            - Fetch ID from blockchain upon creation
            - update data model with ID
        
        """