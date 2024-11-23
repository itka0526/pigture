# Generated by Django 4.2.16 on 2024-11-23 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("marking", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                (
                    "name",
                    models.CharField(
                        db_column="name",
                        help_text="Укажите название",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="images/", verbose_name="изображение"),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "description",
                    models.TextField(blank=True, default="", verbose_name="описание"),
                ),
                (
                    "metadata",
                    models.JSONField(
                        blank=True, default=dict, null=True, verbose_name="метаданные"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="images",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите категорию",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="images",
                        to="marking.category",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="patients.patient",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, help_text="Выберите теги", to="marking.tag"
                    ),
                ),
            ],
            options={
                "verbose_name": "картинка",
                "verbose_name_plural": "картинки",
            },
        ),
        migrations.CreateModel(
            name="Tiles",
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
                ("file", models.FileField(upload_to=images.models.Tiles._upload_to)),
                (
                    "image",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="images.image"
                    ),
                ),
            ],
        ),
    ]
