from pprint import pprint

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, \
    TemplateView
from extra_views import CreateWithInlinesView, InlineFormSetFactory, UpdateWithInlinesView, NamedFormsetsMixin

# from songs.forms import SongForm
# from songs.models import Song, Category

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

#
# class LinkView(InlineFormSetFactory):
#     model = Link
#     fields = "__all__"
#     # prefix = 'item_form'
#     factory_kwargs = {'extra': 3, 'max_num': None, 'can_order': False, 'can_delete': False}
#
#
# class ChordsView(InlineFormSetFactory):
#     model = Chord
#     fields = "__all__"
#     # prefix = 'item_form'
#     factory_kwargs = {'extra': 3, 'max_num': 3, 'can_order': False, 'can_delete': False}


class SongUpdate(PermissionRequiredMixin, UpdateWithInlinesView): #, NamedFormsetsMixin):
    form_class = SongForm
    model = Song
    template_name_suffix = '_update_form'
    permission_required = 'is_staff'
    permission_denied_message = 'Only staff can do this'
    # inlines = [ChordsView, LinkView]
    # inlines_names = ['chord', 'link']

    def get_success_url(self):
        obj_url = reverse('song-detail', kwargs={'pk': self.object.id})
        return obj_url


class SongCreate(PermissionRequiredMixin, CreateWithInlinesView): #, NamedFormsetsMixin):
    form_class = SongForm
    model = Song
    template_name_suffix = '_create_form'
    permission_required = 'is_staff'
    permission_denied_message = 'Only staff can do this'
    # inlines = [ChordsView, LinkView]
    # inlines_names = ['chord', 'link']

    def get_success_url(self):
        obj_url = reverse('song-detail', kwargs={'pk': self.object.id})
        return obj_url
