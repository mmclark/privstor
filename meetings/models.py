from __future__ import unicode_literals

from django.db import models
from private_storage.fields import PrivateFileField

class Meeting(models.Model):
    title = models.CharField(max_length=100)
    meeting_date = models.DateField()
    start_time = models.TimeField()
    description = models.TextField(blank=True)
    agenda = PrivateFileField(upload_to='meetings')


    