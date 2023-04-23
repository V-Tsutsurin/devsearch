from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from PIL import Image
import os


class Photos(models.Model):
    title = models.CharField(max_length=500, verbose_name='Введите заголовок')
    image = models.ImageField(upload_to='additional/images/', verbose_name='Выберите фотографию')
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 800 or img.weight > 400:
            SIZE = (800, 400)
            img.thumbnail(SIZE, Image.LANCZOS)
            img.save(self.image.path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии работ'

