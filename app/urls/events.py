from django.urls import path

from app.views import events

event_urls = [
    path("", events.EventsView.as_view(), name="events"),
]
