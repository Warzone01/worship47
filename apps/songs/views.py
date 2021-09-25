from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from django.db.models import Q
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import SongForm
from .models import Category, Song


class Index(TemplateView):
    template_name = 'worship/index.html'

    def get_context_data(self, **kwargs):
        categs = Category.objects.all()[:4]
        self.extra_context = {'categs': categs}

        kwargs = super(Index, self).get_context_data(**kwargs)
        return kwargs


class SongList(ListView):
    model = Song
    allow_empty = True
    paginate_by = 10
    context_object_name = 'songs'
    queryset = Song.objects.all()
    categ = ''
    search = ''
    qs_length = 0

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return super(SongList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        self.extra_context = {
            'categ': self.categ,
            'search': self.search,
            'search_count': self.qs_length,
        }
        kwargs = super(SongList, self).get_context_data(**kwargs)
        return kwargs

    def get_queryset(self):
        # Filter by categorie's slug
        qs = super(SongList, self).get_queryset()
        self.categ = self.request.GET.get('categ')
        self.search = self.request.GET.get('search')

        if self.search:
            vector = SearchVector(
                'title',
                'title_eng',
                'text',
                'text_eng',
                'author',
            )
            vector_trgm = TrigramSimilarity(
                'title',
                self.search,
            ) + TrigramSimilarity(
                'title_eng',
                self.search,
            ) + TrigramSimilarity(
                'text',
                self.search,
            ) + TrigramSimilarity(
                'text_eng',
                self.search,
            ) + TrigramSimilarity(
                'author',
                self.search,
            )

            qs = qs.annotate(search=vector).filter(search=self.search) or \
                   qs.annotate(similarity=vector_trgm).filter(similarity__gt=0.2)

        elif self.categ:
            qs = qs.filter(category__slug__in=[self.categ])

        self.qs_length = len(qs)
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
