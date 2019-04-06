from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Song, Category, Link
from django.template import loader
from django.db.models import Q


@csrf_exempt
def list(request, categ_slug=''):
    song_list = Song.objects.all().order_by('-category', 'title')
    if request.method == 'POST':
        search = request.POST.get('search', '')
        categ = request.POST.get('categ', '')
        print(search)
        if search:
            if categ:
                song_list = song_list.filter(category_id=categ)
            song_list = song_list.filter(
                Q(title__icontains=search) |
                Q(title_eng__icontains=search)|
                Q(text_eng__icontains=search)|
                Q(text__icontains=search)
            )

        else:
            song_list = Song.objects.none()

    if categ_slug:
        categ = Category.objects.get(slug=categ_slug)
        song_list = song_list.filter(category=categ)

    print(song_list)
    categs = Category.objects.all()
    template = loader.get_template('worship/blog.html')
    context = {
        'song_list': song_list,
        'categs': categs
    }

    return HttpResponse(template.render(context, request))


def song(request, song_id):
    info = get_object_or_404(Song, pk=song_id)
    categs = Category.objects.all()
    context = {
        'info': info,
        'categs': categs,
    }
    return render(request, 'worship/detail.html', context)

