from django import forms
from .models import Song


class SongForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SongForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Song
        exclude = ['created', 'modified']

