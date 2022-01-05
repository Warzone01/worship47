from rest_framework.serializers import ModelSerializer

from songs.models import Song


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        depth = 1
