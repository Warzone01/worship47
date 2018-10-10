from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Song
from django.template import loader
from django.db.models import Q


@csrf_exempt
def index(request):
    if request.method == "GET":
        search = request.GET.get('search', '')
        print(search)
        if search:
            song_list = Song.objects.filter(
                Q(title__icontains=search) | Q(text__icontains=search)
            ).order_by('-category', 'title')
        else:
            song_list = Song.objects.none()
    else:
        song_list = Song.objects.all().order_by('-category', 'title')[:10]

    template = loader.get_template('worship/blog.html')
    context = {
        'song_list': song_list
    }
    return HttpResponse(template.render(context, request))


def song(request, song_id):
    info = get_object_or_404(Song, pk=song_id)
    return render(request, 'worship/detail.html', {'info': info})

