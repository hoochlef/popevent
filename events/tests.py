import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Category, Event, Place


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


# TODO: Write some tests on the discovery view
class DiscoverViewTests(TestCase):
    def test_no_events(self):
        """
        If no events exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("events:discover"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events are available right now.")
        self.assertQuerySetEqual(response.context["latest_event_list"], [])

    def test_events_not_exceeding_five(self):
        """
        If there's more than five events in the database only the latest five are
        displayed in the discovery page.
        """
        category = Category.objects.create(name="Test Category")
        place = Place.objects.create(name="Test Place")

        for i in range(10):
            Event.objects.create(
                title=f"Event {i}",
                content="Test content",
                category=category,
                place=place,
                event_date=timezone.now(),
                author_name="Test Author",
            )

        response = self.client.get(reverse("events:discover"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["latest_event_list"]), 5)