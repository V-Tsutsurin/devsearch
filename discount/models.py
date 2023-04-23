from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from PIL import Image
import os


class Discount(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(upload_to='discount/images/', verbose_name='Выберите изображение', help_text='Картинка должна быть ш.840px на в.720px')
    description = models.TextField(blank=True, verbose_name='Описание')
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 840 or img.weight > 720:
            SIZE = (840, 720)
            img.thumbnail(SIZE, Image.LANCZOS)
            img.save(self.image.path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скидку'
        verbose_name_plural = 'Скидки'


class Slider(models.Model):
    slider = models.ImageField(upload_to='slider/images/', verbose_name='Выберите картинку')
    slider_description = models.TextField(blank=True, verbose_name='Введите описание')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 970 or img.weight > 425:
            SIZE = (970, 425)
            img.thumbnail(SIZE, Image.LANCZOS)
            img.save(self.image.path)


    def __str__(self):
        return self.slider_description

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер'
