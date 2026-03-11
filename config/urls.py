from django.contrib import admin
from django.urls import include, path

from config import settings

urlpatterns = [
    path("", include("events.urls")),
    path("admin/", admin.site.urls),
]

if not settings.TESTING:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
