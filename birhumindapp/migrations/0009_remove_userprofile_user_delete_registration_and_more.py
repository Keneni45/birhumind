# Generated by Django 5.1.1 on 2024-11-11 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("birhumindapp", "0008_event_registration"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Registration",
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]