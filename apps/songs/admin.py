from django.contrib import admin
from django.contrib.admin import register

from .models import Song, Link, Category


class LinkInLine(admin.StackedInline):
    model = Link
    extra = 1

@register(Song)
class SongAdmin(admin.ModelAdmin):
    inlines = [LinkInLine]

# admin.site.register(Song)
admin.site.register(Link)
admin.site.register(Category)
