from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from songs.forms import SongForm
from songs.models import Song


class SongList(ListView):
    model = Song
    allow_empty = False
    paginate_by = 10
    context_object_name = 'songs'
    queryset = Song.objects.all()

    def get_queryset(self):
        # Filter by categorie's slug
        qs = super(SongList, self).get_queryset()
        categ = self.request.GET.get("categ")
        if categ:
            return qs.filter(category__slug__in=[categ])
        else:
            return qs


class SongDetail(LoginRequiredMixin, DetailView):
    model = Song


class SongUpdate(PermissionRequiredMixin, UpdateView):
    form_class = SongForm
    model = Song
    template_name_suffix = '_update_form'
    permission_required = 'is_staff'
    permission_denied_message = 'Only staff can do this'

    def get_success_url(self):
        obj_url = reverse('song-detail', kwargs={'pk': self.object.id})
        return obj_url


class SongCreate(PermissionRequiredMixin, CreateView):
    form_class = SongForm
    model = Song
    template_name_suffix = '_create_form'
    permission_required = 'is_staff'
    permission_denied_message = 'Only staff can do this'

    def get_success_url(self):
        obj_url = reverse('song-detail', kwargs={'pk': self.object.id})
        return obj_url
