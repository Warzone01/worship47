from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from song.models import Song, Category
from users.models import CustomUser
from django.template import loader
from django.db.models import Q


@csrf_exempt
def index(request):
    template = loader.get_template('worship/index.html')  # Отображение шаблона для данной модели(worship)
    categs = Category.objects.all()
    users = CustomUser.objects.all()

    context = {
        'categs': categs,  # Отображение и функциональность категорий в HTML шаблоне
        'users': users,  # Возможность изменять HTML в зависимости от событий (состояния пользователя)
        # 'song_list': song_list,
    }

    return HttpResponse(template.render(context, request))
