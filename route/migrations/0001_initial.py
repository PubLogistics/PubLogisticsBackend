# Generated by Django 4.1.7 on 2023-05-02 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("station", "0001_initial"),
        ("express", "0001_initial"),
        ("line", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliverAddress",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="地址编号"
                    ),
                ),
                ("location", models.CharField(max_length=255, verbose_name="地址位置")),
            ],
        ),
        migrations.CreateModel(
            name="Route",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="路径编号"
                    ),
                ),
                ("from_type", models.BooleanField(default=False, verbose_name="起始点类型")),
                ("to_type", models.BooleanField(default=False, verbose_name="到达点类型")),
                ("step", models.IntegerField(default=0, verbose_name="步骤")),
                ("start_time", models.DateTimeField(blank=True, verbose_name="路程开始时间")),
                ("end_time", models.DateTimeField(blank=True, verbose_name="路程结束时间")),
                (
                    "from_type_0",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_station",
                        to="station.station",
                        verbose_name="站点起始点",
                    ),
                ),
                (
                    "from_type_1",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_location",
                        to="route.deliveraddress",
                        verbose_name="自定起始点",
                    ),
                ),
                (
                    "line",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="line_of_route",
                        to="line.line",
                        verbose_name="使用线路",
                    ),
                ),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="express.package",
                    ),
                ),
                (
                    "to_type_0",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_station",
                        to="station.station",
                        verbose_name="站点结束点",
                    ),
                ),
                (
                    "to_type_1",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_location",
                        to="route.deliveraddress",
                        verbose_name="自定结束点",
                    ),
                ),
            ],
        ),
    ]