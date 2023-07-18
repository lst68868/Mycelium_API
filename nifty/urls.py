from django.contrib import admin
from django.urls import path, include
from main_app.views import NFTViewSet, UserViewSet, CreateUserView, LoginView, LogoutView, CreateNFTView, NFTDetailView, NFTTrendingSet, UserProfileAPIView
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from main_app.views import MyTokenObtainPairView

router = routers.DefaultRouter()
router.register(r'NFT', NFTViewSet, basename='NFT')
router.register(r'users', UserViewSet)
router.register(r'trending', NFTTrendingSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/create-nft/', CreateNFTView.as_view(), name='create_nft'),
    path('nftinfo/<int:tokenId>/', NFTDetailView.as_view(), name='nft_detail'),
    path('api/profile/', UserProfileAPIView.as_view(), name='user_profile'),
    
]