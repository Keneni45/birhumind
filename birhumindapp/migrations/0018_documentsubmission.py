# Generated by Django 5.1.1 on 2024-11-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("birhumindapp", "0017_rename_image_accesstofinance_company_logo"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentSubmission",
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
                ("name", models.CharField(max_length=100)),
                ("education_level", models.CharField(max_length=50)),
                ("institution", models.CharField(max_length=100)),
                ("selected_documents", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
