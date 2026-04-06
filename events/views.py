from django.http import Http404
from django.shortcuts import render

from .models import Event


def index(request):
    return render(request, "events/index.html")


def discover(request):
    """discovery view to display the latest 5 events at the "/discover" path"""
    latest_event_list = Event.objects.order_by("-created_at")[:5]
    context = {"latest_event_list": latest_event_list}
    return render(request, "events/discover.html", context)

def signup(request):
    """account creation function"""
    return render(request, "events/signup.html")

def signin(request):
    """signin function"""
    return render(request, "events/signin.html")


def detail(request, event_id):
    """individual event page details"""
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    # Or use question = get_object_or_404(Question, pk=question_id)

    return render(request, "events/detail.html", {"event": event})
