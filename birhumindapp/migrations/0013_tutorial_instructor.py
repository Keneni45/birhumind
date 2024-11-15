# Generated by Django 5.1.1 on 2024-11-12 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("birhumindapp", "0012_tutorial_details"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tutorial_Instructor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instructor_name", models.CharField(max_length=100)),
                (
                    "instructor_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="instructor_images/"
                    ),
                ),
                ("instructor_title", models.CharField(max_length=200)),
                ("about_instructor", models.TextField()),
            ],
        ),
    ]
