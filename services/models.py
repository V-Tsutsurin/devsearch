from django.db import models


class Servicec(models.Model):
    WORK = (
        ('1', 'Волосы'),
        ('2', 'Ногти'),
        ('3', 'Брови/ресницы'),
    )

    title = models.CharField(max_length=250, verbose_name='Введите название услуги')

    description = models.TextField(verbose_name='Введите описание услуги')
    work_type = models.CharField(max_length=1, choices=WORK, verbose_name='Выберите тип услуги', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
