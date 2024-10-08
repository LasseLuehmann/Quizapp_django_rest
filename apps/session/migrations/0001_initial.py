# Generated by Django 5.1 on 2024-08-22 13:47

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("questions", "0003_remove_question_retried_quiz"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                ("is_correct", models.BooleanField()),
                ("hint", models.BooleanField()),
                ("session_date", models.DateField(default=datetime.datetime.today)),
                ("retry_session", models.BooleanField(default=False)),
                ("session_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "session_questions",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="questions.question",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        to_field="username",
                    ),
                ),
            ],
        ),
    ]
