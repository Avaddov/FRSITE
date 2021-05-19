from django import forms
from . models import MediaObject, GameReview



class MediaObjectForm(forms.ModelForm):
    class Meta:
        model = MediaObject
        exclude = ['author', 'approved']



class GameReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = ['header', 'headline', 'author', 'reviewed_on', 'platforms', 
        'content_block1',  'media_block1', 'content_block2', 'media_block2', 'content_block3', 'summary',  
        'score', 'concept', 'visuals', 'sound', 'playability', 'entertainment_value', 'replay_value'  ]