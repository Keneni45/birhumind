# Generated by Django 5.1.1 on 2024-11-12 06:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("birhumindapp", "0011_remove_tutorial_about_instructor_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tutorial",
            name="details",
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]