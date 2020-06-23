# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django.db import models
from django_extensions.db.models import TimeStampedModel
from pytils import translit
from tagulous.models import TagField
from versatileimagefield.fields import VersatileImageField

def chords_path(instance, filename):
    path = f"chords/{translit.slugify(filename)}"
    return path


def pres_path(instance, filename):
    path = f"presentations/{translit.slugify(filename)}"
    return path


def text_path(instance, filename):
    path = f"text/{translit.slugify(filename)}"
    return path


CHORDS = (
    ("C","C"),
    ("C#","C#"),
    ("D","D"),
    ("D#","D#"),
    ("E","E"),
    ("F","F"),
    ("F#","F#"),
    ("G","G"),
    ("G#","G#"),
    ("A","A"),
    ("A#","A#"),
    ("B","B"),
)

DIFFICULT = (
    ("easy", "Easy"),
    ("medium", "Medium"),
    ("hard", "Hard"),
)


class Category(models.Model):
    title = models.CharField(max_length=50, default='')
    slug = models.CharField(max_length=10, default='')
    image = VersatileImageField(upload_to='categs/')
    priority = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


# class Link(TimeStampedModel):
#     song = models.ForeignKey('Song', on_delete=models.CASCADE,
#                              related_name='ext_links')
#     url = models.CharField(max_length=256, null=True, blank=True)
#     ytb_id = models.CharField(max_length=20, blank=True, null=True,
#                               help_text="Youtube ID for video embedding")
#     description = models.TextField(blank=True, default='')
#
#     def __str__(self):
#         return f"Link for {self.song.title}"
#
#
# class Chord(TimeStampedModel):
#     song = models.ForeignKey('Song', on_delete=models.CASCADE,
#                              related_name='chord_files')
#     chords = models.FileField(upload_to='chords/', blank=True)
#     key = models.CharField(max_length=2, choices=CHORDS,
#                            default="E", blank=True)
#
#     def __str__(self):
#         return f'"{self.key}" chords for {self.song.title}'


class Song(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True)
    title_eng = models.CharField(max_length=255, blank=True)
    text = RichTextField(blank=True)
    text_eng = RichTextField(blank=True)
    chords = RichTextField(blank=True)
    presentation = models.FileField(upload_to=pres_path, blank=True)
    text_file = models.FileField(upload_to=text_path, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    author = models.CharField(max_length=100, blank=True, default='')
    is_translated = models.BooleanField(blank=True, default=True)
    translator = TagField(
        max_count=6,
        initial=['Фурманов', 'Зуев', 'Иваник', 'Куга', 'Жданов', 'Герасимович'],
        blank=True,
    )
    main_key = models.CharField(max_length=2, choices=CHORDS,
                                default="E", blank=True)
    difficult = models.CharField(max_length=6, choices=DIFFICULT,
                                 default="easy", blank=True)

    chordsFile1 = models.FileField(upload_to=chords_path, blank=True)
    chordKey1 = models.CharField(max_length=2, choices=CHORDS,
                            default="E", blank=True)
    chordsFile2 = models.FileField(upload_to=chords_path, blank=True)
    chordKey2 = models.CharField(max_length=2, choices=CHORDS,
                            default="E", blank=True)

    ytb_id1 = models.CharField(max_length=100, blank=True)
    ytb_id2 = models.CharField(max_length=100, blank=True)
    ytb_id3 = models.CharField(max_length=100, blank=True)


    class Meta:
        ordering = ['id']

    def __str__(self):
        if self.title_eng:
            return f"{self.title} | {self.title_eng}"
        else:
            return self.title
