from ckeditor.fields import RichTextField
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from pytils import translit


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='name', editable=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def slugify_function(self, value):
        return translit.slugify(value)

    def __str__(self):
        return self.name


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

    class Meta:
        ordering = ['id']

    def __str__(self):
        if self.title_eng:
            return f"{self.title} | {self.title_eng}"
        else:
            return self.title
