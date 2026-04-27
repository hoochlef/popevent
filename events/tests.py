import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Event


class EventModelTests(TestCase):
    def test_was_created_recently_with_future_event(self):
        """
        was_created_recently() returns False for events whose created_at is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_event = Event(created_at=time)
        self.assertIs(future_event.was_created_recently(), False)

    def test_was_created_recently_with_old_event(self):
        """
        was_created_recently() returns False for events whose created_at is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_event = Event(created_at=time)
        self.assertIs(old_event.was_created_recently(), False)

    def test_was_created_recently_with_recent_event(self):
        """
        was_created_recently() returns True for events whose created_at is within the past 24hrs.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_event = Event(created_at=time)
        self.assertIs(recent_event.was_created_recently(), True)
