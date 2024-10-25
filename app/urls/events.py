from django.urls import path

from app.views import events

event_urls = [
    path("", events.EventsView.as_view(), name="events"),
    path("participants/", events.EventParticipantAPIView.as_view(), name="participants"),
    path("participant/<str:code>/", events.EventParticipantDetailAPIView.as_view(), name="participant_detail"),
]
