from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
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

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return super(SongList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        self.extra_context = {'categ': self.categ}
        kwargs = super(SongList, self).get_context_data(**kwargs)
        return kwargs

    def get_queryset(self):
        # Filter by categorie's slug
        qs = super(SongList, self).get_queryset()
        self.categ = self.request.GET.get("categ")
        search = self.request.GET.get("search")
        if search:
            qs = qs.filter(
                Q(text__icontains=search) |
                Q(text_eng__icontains=search)
            )
        elif self.categ:
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
