from django.db import models
import time

class Dog(models.Model):

    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    img = models.CharField(max_length=250)
    good_dog = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

# dogs model: breed 'name', AKC 'type', image, good_dog, created_at

