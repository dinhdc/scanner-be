from rest_framework import serializers
from app.models import School, Event, EventParticipator
from .users import UserSerializer
from .schools import SchoolSerializer


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Event
        exclude = ['created_by']


class EventParticipantSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = EventParticipator
        fields = '__all__'
