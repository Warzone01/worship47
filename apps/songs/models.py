from ckeditor.fields import RichTextField
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.template.defaultfilters import slugify as django_slugify
from django_extensions.db.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='name', slugify_function=django_slugify)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.slug


class Link(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return f"Link for {self.song.title}"


class Song(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True)
    title_eng = models.CharField(max_length=255, blank=True)
    text = RichTextField(blank=True)
    text_eng = RichTextField(blank=True)
    accords = RichTextField(blank=True)
    presentation = models.FileField(upload_to='presentations/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.title_eng:
            return f"{self.title} | {self.title_eng}"
        else:
            return self.title
