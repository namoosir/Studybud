from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message

class StudyBudAdminArea(admin.AdminSite):
    index_title = "StudyBud"
    site_header = "StudyBud Admin"
    site_title = "StudyBud Admin"

studybud_admin_site = StudyBudAdminArea()

studybud_admin_site.register(Room)
studybud_admin_site.register(Topic)
studybud_admin_site.register(Message)

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
