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
