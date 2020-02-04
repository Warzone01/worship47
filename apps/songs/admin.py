from django.contrib import admin
from django.contrib.admin import register
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from tagulous import admin as tagadmin
import threading
from .models import Song, Link, Chord, Category


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" style="width: 150px;"/></a> %s ' % \
                      (image_url, image_url, file_name, 'Change:'))
        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))


class ImageWidgetAdmin(admin.ModelAdmin):
    image_fields = []

    def __init__(self, model, admin_site):
        self.request = None
        super().__init__(model, admin_site)

    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request)

    @property
    def base_url(self):
        return f'{self.request.scheme}://{self.request.META.get("HTTP_HOST")}'

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.image_fields:
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageWidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)


@register(Category)
class CategAdmin(ImageWidgetAdmin):
    list_display = ['priority', 'slug', 'title', 'admin_image']
    list_display_links = ['slug']
    list_editable = ['priority']
    image_fields = ['image']

    def admin_image(self, obj):
        try:
            url = f'{obj.image.url}'
        except:
            url = f"{obj.image}"
        return mark_safe(f'<img src="{self.base_url}{url}" style="width: 50px;"/>')

    admin_image.allow_tags = True


class LinkInLine(admin.StackedInline):
    model = Link
    extra = 0


class ChordInLine(admin.StackedInline):
    model = Chord
    extra = 0


class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_eng', 'categ']
    inlines = [LinkInLine, ChordInLine]

    def categ(self, obj):
        categs = []
        for c in obj.category.all():
            categs.append(f"{c.title} ({c.slug})")
        return ' || '.join(categs)


tagadmin.register(Song, SongAdmin)
admin.site.register(Link)
admin.site.register(Chord)
