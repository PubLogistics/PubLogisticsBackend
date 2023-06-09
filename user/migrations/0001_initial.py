# Generated by Django 4.1.7 on 2023-05-02 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="profile",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
                ("nickname", models.CharField(max_length=64, verbose_name="用户昵称")),
                ("conductor", models.BooleanField(default=False, verbose_name="司乘权限")),
                (
                    "wage",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=6,
                        verbose_name="钱",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="company.company",
                        verbose_name="所在公司",
                    ),
                ),
            ],
        ),
    ]
