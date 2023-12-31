# Generated by Django 4.1.10 on 2023-07-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hello_world", "0002_defaultchatsettings"),
    ]

    operations = [
        migrations.AddField(
            model_name="defaultchatsettings",
            name="description",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="defaultchatsettings",
            name="role",
            field=models.CharField(
                choices=[
                    ("system", "System"),
                    ("assistant", "Assistant"),
                    ("user", "User"),
                ],
                max_length=50,
            ),
        ),
    ]
