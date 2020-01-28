from django import forms
from .models import Song, Media


class SongForm(forms.ModelForm):


    class Meta:
        model = Song
        model2 = Media
        exclude = ['created', 'modified']

