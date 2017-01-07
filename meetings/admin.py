from django.contrib import admin
from .models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'meeting_date', 'start_time')

admin.site.register(Meeting, MeetingAdmin)
    