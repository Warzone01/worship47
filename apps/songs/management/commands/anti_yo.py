from django.core.management.base import BaseCommand

from songs.models import Song
from songs.services import AntiYoService


class Command(BaseCommand):
    help = 'Cleanup YO chars in textxs and titles'

    def handle(self, *args, **options):
        all_songs = Song.objects.all()
        counter = 0
        for song in all_songs:
            text = song.text
            title = song.title
            fields_to_save = []
            if new_title := AntiYoService().cleanup_yo(title):
                if new_title != title:
                    song.title = new_title
                    fields_to_save.append('title')

            if new_text := AntiYoService().cleanup_yo(text):
                if new_text != text:
                    song.text = new_text
                    fields_to_save.append('text')

            if fields_to_save:
                song.save(update_fields=fields_to_save)
                print(song.id, fields_to_save)
                counter += 1

        print(f'Fixed {counter} songs')
