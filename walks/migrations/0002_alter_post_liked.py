# Generated by Django 5.0.6 on 2024-05-29 21:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("walks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="liked",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name="liked_posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
