# Generated by Django 4.2.9 on 2024-01-07 09:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0002_topic_room_host_message_room_topic"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room", options={"ordering": ["-updated", "-created"]},
        ),
        migrations.AddField(
            model_name="room",
            name="participants",
            field=models.ManyToManyField(
                blank=True, related_name="participants", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
