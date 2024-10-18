from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name='User'
    )
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    checkin_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tickets'

    def generate_code(self):
        dt_str = datetime.now().strftime("%d%m%y")
        _id = self.pk
        code = f"TK{dt_str}-{_id:04d}"
        self.code = code
        self.save()
