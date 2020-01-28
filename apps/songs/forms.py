from django import forms
from .models import Song, Media


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        exclude = ['created', 'modified']

