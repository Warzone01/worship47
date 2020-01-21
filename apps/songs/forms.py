from django import forms
from .models import Song
from .models import Link


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        exclude = ['created', 'modified']

