from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import SongForm
from .models import Category, Song
from .services import AntiYoService


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

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        self.categ = self.request.GET.get('categ')
        self.search = self.request.GET.get('search')
        return super(SongList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        self.extra_context = {
            'categ': self.categ,
            'search': self.search,
        }
        kwargs = super(SongList, self).get_context_data(**kwargs)
        return kwargs

    def get_queryset(self):
        qs = super(SongList, self).get_queryset()
        qs = qs.prefetch_related('category')

        if self.search:
            self.search = AntiYoService().cleanup_yo(self.search)
            search_vector = SearchVector(
                'title',
                'title_eng',
                'text',
                'text_eng',
                'author',
            )
            search_query = SearchQuery(
                self.search,
            )
            search_rank = SearchRank(search_vector, search_query)

            qs = qs.annotate(
                search=search_vector,
                rank=search_rank,
            ).filter(
                search=search_query,
                rank__gte=0.5,
            ).order_by(
                '-rank',
            )

        # Filter by categorie's slug
        if self.categ:
            qs = qs.filter(category__slug__in=[self.categ])

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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.title = AntiYoService().cleanup_yo(obj.title)
            obj.text = AntiYoService().cleanup_yo(obj.text)
            obj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



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

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.title = AntiYoService().cleanup_yo(obj.title)
            obj.text = AntiYoService().cleanup_yo(obj.text)
            obj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
