import datetime

from django.db import models
from django.contrib.auth.models import User
from .schools import School


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    school = models.ForeignKey(School, on_delete=models.CASCADE,
                               related_name='events', related_query_name='events')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   null=True, blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'events'


class EventParticipator(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='participators', related_query_name='participators')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True)
    checkin_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participator_inviter', null=True,
                                   blank=True)
    checkin_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participator_scanner', null=True,
                                   blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'event_participators'

    def generate_code(self):
        dt_str = self.event.start_date.strftime("%d%m%y")
        _id = self.pk
        code = f"EP{dt_str}-{_id:04d}"
        self.code = code
        self.save()
