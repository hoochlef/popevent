from django.urls import path

from . import views

app_name = "events"
urlpatterns = [
    path("", views.index, name="index"),
    path("discover", views.discover, name="discover"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("event/<int:event_id>/", views.detail, name="detail"),
]
