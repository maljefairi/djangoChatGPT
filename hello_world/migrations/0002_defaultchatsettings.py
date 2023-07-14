# Generated by Django 4.1.10 on 2023-07-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hello_world", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DefaultChatSettings",
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
                ("role", models.CharField(default="user", max_length=255)),
            ],
        ),
    ]