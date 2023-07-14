from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

<<<<<<< HEAD
class NFT(models.Model):
    title = models.CharField(max_length=256)
    creator = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)
    image_link = models.CharField(max_length=256)
    owned_by = models.CharField(max_length=256)
    category = models.CharField(max_length=256, default='')
=======
# Create your models here.
class NFT_blockchain_data(models.Model):
    creator = models.CharField(max_length=256) #ETH address of creator who executed the minting transaction
    date_created = models.DateTimeField(auto_now_add=True)
    image_link = models.CharField(max_length=256) #Weblink
    owner = models.CharField(max_length=256) #ETH address of current owner
    
    def __str__(self):
        return f'{self.title} by {self.creator} --- owned by {self.owner}'
    
class NFT_platform_data(models.Model):
    title = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
>>>>>>> matt
    
    
    def __str__(self):
        return f'{self.title} by {self.creator} --- owned by {self.owned_by}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ethereum_address = models.CharField(max_length=42)  # Ethereum addresses are 42 characters long

    def __str__(self):
<<<<<<< HEAD
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
=======
        return f'{self.title} by {self.creator} --- owned by {self.owned_by}'
    
    
#User model is already defined in django.contrib.auth.models
#But we need to add a field to it

#User model

#ETH_address_linked = models.CharField(max_length=256) #ETH address
>>>>>>> matt
