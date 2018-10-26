from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name='index'),
    path('<int:song_id>/', views.song, name='song'),
    path('categ/<slug:categ_slug>/', views.list, name='categ'),
]
