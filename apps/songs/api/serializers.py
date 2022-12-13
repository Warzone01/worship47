from songs.models import Song
from rest_framework.serializers import ModelSerializer


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        depth = 1
