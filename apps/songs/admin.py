from django.contrib import admin
from django.contrib.admin import register

from .models import Song, Link, Category


class LinkInLine(admin.StackedInline):
    model = Link
    extra = 1

@register(Song)
class SongAdmin(admin.ModelAdmin):
    inlines = [LinkInLine]


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    list_display_links = ['slug']


admin.site.register(Link)
