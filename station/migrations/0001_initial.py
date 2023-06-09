# Generated by Django 4.1.7 on 2023-05-02 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("line", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StationName",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="车站名列表编号"
                    ),
                ),
                ("name", models.CharField(max_length=64, verbose_name="车站名")),
                (
                    "id_in_line",
                    models.CharField(blank=True, max_length=5, verbose_name="线内编号"),
                ),
                (
                    "line",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="station_on_line",
                        to="line.line",
                        verbose_name="所属线路",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Station",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="车站编号"
                    ),
                ),
                (
                    "direction",
                    models.CharField(blank=True, max_length=32, verbose_name="行驶方向"),
                ),
                (
                    "location",
                    models.CharField(blank=True, max_length=255, verbose_name="车站位置"),
                ),
                (
                    "name",
                    models.ManyToManyField(
                        related_name="station_name",
                        to="station.stationname",
                        verbose_name="车站名称",
                    ),
                ),
            ],
        ),
    ]
