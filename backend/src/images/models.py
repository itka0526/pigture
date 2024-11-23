from django.db import models

import marking.models


class Image(models.Model):
    image = models.ImageField(verbose_name='изображение', upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        marking.models.Category,
        help_text='Выберите категорию',
        on_delete=models.SET_NULL,
        related_name='images',
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        marking.models.Tag,
        blank=True,
        help_text='Выберите теги',
    )

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'

    def __str__(self):
        return f'{self.image.name} - {self.uploaded_at}'
