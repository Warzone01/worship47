from django import forms
from songs.models import Song


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        exclude = ['created', 'modified']

