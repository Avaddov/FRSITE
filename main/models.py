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
    header = models.ImageField(null=True)
    game_title = models.CharField(max_length=200, null=True)
    headline = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    publish_date = models.DateTimeField(null=True)
    publisher = models.CharField(max_length=200, null=True)
    developer = models.CharField(max_length=200, null=True)
    first_release_date = models.DateTimeField(null=True)
    release_date = models.DateTimeField(null=True)
    reviewed_on = models.CharField(max_length=100, null=True)
    platforms = models.CharField(max_length=200, null=True)
    content_block1 = models.TextField(null=True)
    media_block1 = models.ImageField(null=True)
    content_block2 = models.TextField(null=True)
    media_block2 = models.ImageField(null=True)
    content_block3 = models.TextField(null=True)
    summary = models.TextField(null=True)
    score = models.FloatField(null=True)
    concept = models.TextField(null=True)
    visuals = models.TextField(null=True)
    sound = models.TextField(null=True)
    playability = models.TextField(null=True)
    entertainment_value = models.TextField(null=True)
    replay_value = models.TextField(null=True)
    url = models.URLField(null=True)
    # score
    


    def __str__(self):
        return self.game_title



# Video
# Screenshots
# Rating
# Graphics