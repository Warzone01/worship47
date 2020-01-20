from django.contrib import admin
from django.contrib.admin import register
from .models import Song, Link


class LinkInLine(admin.StackedInline):
    model = Link
    extra = 1


@register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_eng', 'categ']
    inlines = [LinkInLine]

    def categ(self, obj):
        categs = []
        for c in obj.category.all():
            categs.append(f"{c.name} ({c.slug})")
        return ' || '.join(categs)

admin.site.register(Link)
