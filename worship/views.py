from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from song.models import Song, Category
from django.template import loader
from django.db.models import Q


@csrf_exempt
def index(request):
    template = loader.get_template('worship/index.html')
    categs = Category.objects.all()

    context = {
        'categs': categs,
        # 'song_list': song_list,
    }

    return HttpResponse(template.render(context, request))


def Registration(request):

    return None
