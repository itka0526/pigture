# Generated by Django 4.2.16 on 2024-11-22 16:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="image",
            options={
                "verbose_name": "картинка",
                "verbose_name_plural": "картинки",
            },
        ),
    ]
