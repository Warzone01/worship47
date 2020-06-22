from django import forms
from extra_views import InlineFormSetFactory, UpdateWithInlinesView, CreateWithInlinesView, ModelFormSetView, \
    FormSetView, InlineFormSetView
from extra_views.generic import GenericInlineFormSetView

from .models import Song, Link


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        exclude = ['created', 'modified']


#
# class CreateFields(CreateWithInlinesView):
#     model = Song
#     inlines = [ChordsView, LinkView]
#     # template_name = 'songs/song_create_form.html'
#
#
# class UpdateFields(UpdateWithInlinesView):
#     model = Song
#     inlines = [ChordsView, LinkView]
#     # template_name = 'songs/song_update_form.html'


# class FormSet(FormSetView):
#     form_class = LinkForm
#     template_name = 'song_create_form.html'






