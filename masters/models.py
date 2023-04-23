from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from PIL import Image
import os



class Master(models.Model):
    LOCATION = (
        ('1', 'Шишкина'),
        ('2', 'Заречная')
    )
    photo = models.ImageField(upload_to='masters/images/', verbose_name='Выберите изображение')
    name = models.CharField(max_length=200, verbose_name='Введите имя мастера')
    specialization = models.TextField(verbose_name='Введите направление деятельности мастера')
    link = models.URLField(verbose_name='Ссылка на мастера')
    location = models.CharField(max_length=1, choices=LOCATION, verbose_name='Выберите место работы мастера')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)

        if img.height > 169 or img.weight > 171:
            SIZE = (169, 171)
            img.thumbnail(SIZE, Image.LANCZOS)
            img.save(self.photo.path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мастера'
        verbose_name_plural = 'Мастера'
