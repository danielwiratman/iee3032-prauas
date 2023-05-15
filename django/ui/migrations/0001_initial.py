# Generated by Django 4.2.1 on 2023-05-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensor",
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
                ("pabrik", models.IntegerField()),
                ("subsistem", models.IntegerField()),
                ("name", models.CharField(max_length=100)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
