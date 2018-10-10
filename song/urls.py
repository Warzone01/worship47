from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:song_id>/', views.song, name='song'),
]
