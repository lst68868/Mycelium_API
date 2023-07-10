from django.contrib import admin
from django.urls import path, include
from main_app.views import NFTViewSet, UserViewSet
from rest_framework import routers
from main_app.views import LoginView


router = routers.DefaultRouter()
router.register(r'NFT', NFTViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]