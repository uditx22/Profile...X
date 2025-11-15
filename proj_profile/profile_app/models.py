from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=300)
    profile_pic = models.ImageField(upload_to="profile_app/images")
    location = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    
    def __str__(self): 
        return f"{self.name}"