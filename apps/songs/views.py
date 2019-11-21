from django.shortcuts import render
from django.views.generic import ListView, DetailView

from songs.models import Song


class SongList(ListView):
    model = Song
    paginate_by = 10
    context_object_name = 'songs'


class SongDetail(DetailView):
    model = Song

