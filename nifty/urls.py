from django.contrib import admin
from django.urls import path, include
from main_app.views import NFTViewSet, UserViewSet, CreateUserView, LoginView, LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'NFT', NFTViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('api-auth/', include('rest_framework.urls')),
]
