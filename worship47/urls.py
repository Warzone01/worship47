from songs.views import Index

from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # path('', TemplateView.as_view(template_name='worship/index.html'), name='home'),
    path('', Index.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('songs/', include('songs.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('accounts.api.urls')),
    path('api/', include(('songs.api.urls', 'songs'), namespace='api-songs')),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
