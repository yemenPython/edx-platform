"""
Django Admin for Notifications
"""

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Notification


class NotificationAdmin(SimpleHistoryAdmin):
    pass

admin.site.register(Notification, NotificationAdmin)
