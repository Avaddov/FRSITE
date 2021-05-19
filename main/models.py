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
    header = models.ImageField(null=True, blank=True)
    cover = models.URLField(null=True, blank=True)
    game_title = models.CharField(max_length=200, null=True, blank=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField(max_length=200, null=True, blank=True)
    developer = models.CharField(max_length=200, null=True, blank=True)
    first_release_date = models.DateTimeField(null=True, blank=True)
    release_date = models.DateTimeField(null=True, blank=True)
    reviewed_on = models.CharField(max_length=100, null=True, blank=True)
    platforms = models.CharField(max_length=200, null=True, blank=True)
    content_block1 = models.TextField(null=True, blank=True)
    media_block1 = models.ImageField(null=True, blank=True)
    content_block2 = models.TextField(null=True, blank=True)
    media_block2 = models.ImageField(null=True, blank=True)
    content_block3 = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    concept = models.TextField(null=True, blank=True)
    visuals = models.TextField(null=True, blank=True)
    sound = models.TextField(null=True, blank=True)
    playability = models.TextField(null=True, blank=True)
    entertainment_value = models.TextField(null=True, blank=True)
    replay_value = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    # score
    


    def __str__(self):
        return self.game_title



# Video
# Screenshots
# Rating
# Graphics