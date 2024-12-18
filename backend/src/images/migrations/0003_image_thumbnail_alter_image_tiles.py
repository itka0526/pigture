# Generated by Django 4.2.16 on 2024-11-24 09:35

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_tiles_delete_tiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='tiles',
            field=models.FileField(blank=True, null=True, upload_to=images.models._upload_tile),
        ),
    ]
