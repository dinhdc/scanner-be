from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'schools'
