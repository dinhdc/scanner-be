from rest_framework import serializers

from app.models import Ticket
from app.serializers.user import UserSerializer


class TicketResSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['title', 'user']

    def create(self, validated_data):
        # user = validated_data.pop('user')
        ticket = super().create(validated_data)
        # ticket.user = user
        ticket.save()
        ticket.generate_code()
        return ticket


class TicketCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['code']
