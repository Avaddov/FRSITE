from django import forms
from . models import MediaObject



class MediaObjectForm(forms.ModelForm):
    class Meta:
        model = MediaObject
        exclude = ['author', 'approved']
