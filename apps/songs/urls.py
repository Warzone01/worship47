from django.urls import path, include
from songs.views import SongList, SongDetail, SongUpdate, SongCreate

urlpatterns = [
    path('list/', SongList.as_view(), name='songs-list-first'),
    path('list/<int:page>/', SongList.as_view(), name='songs-list'),
    path('song/<int:pk>/', SongDetail.as_view(), name='song-detail'),
    path('song/<int:pk>/edit/', SongUpdate.as_view(), name='song-update'),
    path('song/', SongCreate.as_view(), name='song-create'),
]
