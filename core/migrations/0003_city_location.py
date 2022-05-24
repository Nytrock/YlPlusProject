# Generated by Django 4.0.4 on 2022-05-24 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_contact_contacts_group_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("query", models.CharField(max_length=250, verbose_name="Адрес")),
                ("fias", models.CharField(max_length=50, verbose_name="ФИАС")),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.city", verbose_name="Город"
                    ),
                ),
            ],
            options={
                "verbose_name": "Местоположение",
                "verbose_name_plural": "Местоположения",
            },
        ),
    ]
