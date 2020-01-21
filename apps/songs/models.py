# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django.db import models
from django_extensions.db.models import TimeStampedModel
from tagulous.models import TagField
from autoslug import AutoSlugField


class Link(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return "Link for {self.song.title}"


class Song(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True)
    title_eng = models.CharField(max_length=255, blank=True)
    text = RichTextField(blank=True)
    text_eng = RichTextField(blank=True)
    accords = RichTextField(blank=True)
    presentation = models.FileField(upload_to='presentations/', blank=True)
    accords_dwnl = models.FileField(upload_to='accords/', blank=True)
    text_dwnl = models.FileField(upload_to="text/", blank=True)
    category = TagField(
        force_lowercase=False,
        max_count=4,
        initial=['Общие', 'Рождественские', 'Пасхальные', 'Детские'],
        blank=True,
    )
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, default='')
    is_translated = models.BooleanField(blank=True, default=True)
    translator = TagField(
        force_lowercase=False,
        max_count=6,
        initial=['Фурманов', 'Зуев', 'Иваник', 'Куга', 'Жданов', 'Герсимович'],
        blank=True,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        if self.title_eng:
            return f"{self.title} | {self.title_eng}"
        else:
            return self.title
