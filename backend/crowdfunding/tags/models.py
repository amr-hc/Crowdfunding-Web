 

from django.db import models
# Create your models here.
class Tag (models.Model):
    tagName = models.CharField(max_length=100,blank=True)
    
    
    def __str__(self):
        return f'{self.tagName}'
    
   
