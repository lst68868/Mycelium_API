from django.db import models

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
    
    def __str__(self):
        return f'{self.title} by {self.creator} --- owned by {self.owned_by}'
    
    
#User model is already defined in django.contrib.auth.models
#But we need to add a field to it

#User model

#ETH_address_linked = models.CharField(max_length=256) #ETH address