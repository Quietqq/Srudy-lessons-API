# Generated by Django 4.2.5 on 2023-10-10 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0002_alter_lessonviewinfo_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="lessonviewinfo",
            name="last_view_datetime",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 10, 16, 5, 3, 54697)
            ),
        ),
    ]
