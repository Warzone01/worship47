from django.urls import path, include
from songs.views import SongList, SongDetail

urlpatterns = [
    path('list/', SongList.as_view(), name='songs-list-first'),
    path('list/<int:page>/', SongList.as_view(), name='songs-list'),
    path('detail/<int:pk>/', SongDetail.as_view(), name='song-detail'),

]
