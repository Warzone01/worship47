from typing import Any

from pytils import translit
from accounts.models import User
from ckeditor.fields import RichTextField
from tagulous.models import TagField
from versatileimagefield.fields import VersatileImageField

from django.db import models


def chords_path(instance: Any, filename: str) -> str:
    ext = filename.split('.')[-1:]
    fname = filename[:filename.rfind('.')]
    path = f'chords/{translit.slugify(fname)}.{str(ext)}'
    return path


def pres_path(instance: Any, filename: str) -> str:
    ext = filename.split('.')[-1:]
    fname = filename[:filename.rfind('.')]
    path = f'presentations/{translit.slugify(fname)}.{str(ext)}'
    return path


def text_path(instance: Any, filename: str) -> str:
    ext = filename.split('.')[-1:]
    fname = filename[:filename.rfind('.')]
    path = f'text/{translit.slugify(fname)}.{str(ext)}'
    return path


CHORDS = (
    ('C', 'C'),
    ('C#', 'C#'),
    ('D', 'D'),
    ('D#', 'D#'),
    ('E', 'E'),
    ('F', 'F'),
    ('F#', 'F#'),
    ('G', 'G'),
    ('G#', 'G#'),
    ('A', 'A'),
    ('A#', 'A#'),
    ('B', 'B'),
)

DIFFICULT = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
)


class Category(models.Model):
    title = models.CharField(max_length=50, default='')
    slug = models.CharField(max_length=10, default='')
    image = VersatileImageField(upload_to='categs/')
    priority = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title


class Song(models.Model):
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
                                default='E', blank=True)
    difficult = models.CharField(max_length=6, choices=DIFFICULT,
                                 default='easy', blank=True)

    chordsFile1 = models.FileField(upload_to=chords_path, blank=True)
    chordKey1 = models.CharField(
        max_length=2,
        choices=CHORDS,
        default='E',
        blank=True,
    )
    chordsFile2 = models.FileField(upload_to=chords_path, blank=True)
    chordKey2 = models.CharField(
        max_length=2,
        choices=CHORDS,
        default='E',
        blank=True,
    )

    ytb_id1 = models.CharField(max_length=100, blank=True)
    ytb_id2 = models.CharField(max_length=100, blank=True)
    ytb_id3 = models.CharField(max_length=100, blank=True)

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        if self.title_eng:
            return f'{self.title} | {self.title_eng}'
        else:
            return self.title
