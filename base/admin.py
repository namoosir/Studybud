from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message

class RoomAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Required', {
            "fields": (
                "host",
                "topic",
                "name",
            ),
        }),
        ('Optional', {
            "fields": (
                "description",
                "participants",
            ),
        }),
    )

admin.site.register(Room, RoomAdmin)
admin.site.register(Topic)
admin.site.register(Message)
