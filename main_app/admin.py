from django.contrib import admin
from .models import NFT
from .models import Profile

# Register your models here.
admin.site.register(NFT)
admin.site.register(Profile)