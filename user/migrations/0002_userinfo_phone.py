# Generated by Django 4.1.7 on 2023-05-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="phone",
            field=models.CharField(
                blank=True, max_length=13, null=True, verbose_name="电话号码"
            ),
        ),
    ]
