# Generated by Django 5.1 on 2024-09-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="poster",
            field=models.ImageField(blank=True, null=True, upload_to="poster_image/"),
        ),
    ]
