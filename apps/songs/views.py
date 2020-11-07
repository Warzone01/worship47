from pprint import pprint

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, \
    TemplateView

from .forms import SongForm
from .models import Category, Song #, Chord, Link


class Index(TemplateView):
    template_name = 'worship/index.html'

    def get_context_data(self, **kwargs):
        categs = Category.objects.all()[:4]
        self.extra_context = {'categs': categs}

        kwargs = super(Index, self).get_context_data(**kwargs)
        return kwargs


class SongList(ListView):
    model = Song
    allow_empty = False
    paginate_by = 10
    context_object_name = 'songs'
    queryset = Song.objects.all()

    def get_context_data(self, **kwargs):
        self.extra_context = {'categ': self.categ}

        kwargs = super(SongList, self).get_context_data(**kwargs)
        return kwargs

    def get_queryset(self):
        # Filter by categorie's slug
        qs = super(SongList, self).get_queryset()
        self.categ = self.request.GET.get("categ")
        if self.categ:
            return qs.filter(category__slug__in=[self.categ])
        else:
            return qs


class SongDetail(LoginRequiredMixin, DetailView):
    model = Song


class SongUpdate(PermissionRequiredMixin, UpdateView):
    form_class = SongForm
    model = Song
    template_name_suffix = '_update_form'
    permission_required = ('songs.add_song', 'songs.change_song')
    permission_denied_message = 'Only staff can do this'

    def get_success_url(self):
        obj_url = reverse('song-detail', kwargs={'pk': self.object.id})
        return obj_url


class SongCreate(PermissionRequiredMixin, CreateView):
    form_class = SongForm
    model = Song
    template_name_suffix = '_create_form'
    permission_required = ('songs.add_song', 'songs.change_song')
    permission_denied_message = 'Only staff can do this'

    def get_success_url(self):
        obj_url = reverse('song-detail', kwargs={'pk': self.object.id})
        return obj_url

    def get_form_kwargs(self):
        kwargs = super(SongCreate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
