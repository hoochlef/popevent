from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("discover", views.discover, name="discover"),
    path("event/<int:event_id>/", views.detail, name="detail"),
]
