from ckeditor.fields import RichTextField
from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField('Name', max_length=20, null=True)
    slug = AutoSlugField(populate_from='name', null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null="True", blank=True)


class Song(models.Model):
    title = models.CharField(max_length=200, blank=True)
    title_eng = models.CharField(max_length=200, blank=True)
    text = RichTextField(blank=True)
    text_eng = RichTextField(blank=True)
    accords = RichTextField(blank=True)
    presentation = models.FileField(upload_to='presentations/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title



