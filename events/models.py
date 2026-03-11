import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "places"

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)

    content = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="events",
    )

    place = models.ForeignKey(
        Place,
        on_delete=models.PROTECT,
        related_name="events",
    )

    event_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    # Updates to the current time every time the object is saved.
    updated_at = models.DateTimeField(auto_now=True)

    author_name = models.CharField(
        max_length=200,
        help_text="Free-form author name for v0 (no auth yet)",
    )

    class Meta:
        db_table = "events"

    def __str__(self):
        return self.title

    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
