# Generated by Django 4.2.16 on 2024-11-24 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', help_text='Укажите название заметки', max_length=150, verbose_name='название')),
                ('description', models.TextField(blank=True, default='', verbose_name='описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='images.image')),
            ],
            options={
                'verbose_name': 'заметка',
                'verbose_name_plural': 'заметки',
            },
        ),
    ]
