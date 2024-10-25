from rest_framework import serializers
from app.models import School, Event
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