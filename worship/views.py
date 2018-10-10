from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from song.models import Song
from django.template import loader
from django.db.models import Q
# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        print(search)
        if search:
            song_list = Song.objects.filter(Q(title__icontains=search) | Q(text__icontains=search)).order_by('-category', 'title')
        else:
            song_list = Song.objects.none()
    else:
        song_list = Song.objects.all().order_by('-category', 'title')

    template = loader.get_template('worship/index.html')

    context = {
        'song_list': song_list
    }

    return HttpResponse(template.render(context, request))

