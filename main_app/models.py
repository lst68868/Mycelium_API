from django.db import models

# Create your models here.
class NFT(models.Model):
    title = models.CharField(max_length=256)
    creator = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)
    image_link = models.CharField(max_length=256)
    owned_by = models.CharField(max_length=256)
    
    def __str__(self):
        return f'{self.title} by {self.creator} --- owned by {self.owned_by}'