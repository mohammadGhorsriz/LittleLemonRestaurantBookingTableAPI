# Generated by Django 5.0.1 on 2024-01-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("no_of_guests", models.SmallIntegerField()),
                ("bookingDate", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                (
                    "id",
                    models.SmallIntegerField(
                        primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("inventory", models.SmallIntegerField()),
            ],
        ),
    ]
