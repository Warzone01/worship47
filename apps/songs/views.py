from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from songs.forms import SongForm
from songs.models import Song


class SongList(ListView):
    model = Song
    paginate_by = 10
    context_object_name = 'songs'


class SongDetail(DetailView):
    model = Song


class SongUpdate(UpdateView):
    form_class = SongForm
    model = Song
    template_name_suffix = '_update_form'

    def get_success_url(self):
        obj_url = reverse('song-detail', kwargs={'pk': self.object.id})
        return obj_url


class SongCreate(CreateView):
    form_class = SongForm
    model = Song
    template_name_suffix = '_create_form'
    # success_url = reverse('songs-list-first')

    def get_success_url(self):
        obj_url = reverse('song-detail', kwargs={'pk': self.object.id})
        return obj_url
