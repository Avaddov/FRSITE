from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class MediaCategory(models.Model):
    name = models.CharField(max_length=200)
        
    def __str__(self):
        return self.name

    


class MediaObject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE, null=True)



    
    def __str__(self):
        return self.title



class GameReview(models.Model):
    game_title = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    content = models.TextField()


    def __str__(self):
        return self.game_title

