# Generated by Django 4.2b1 on 2023-04-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0002_slider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': 'Скидка', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайдер'},
        ),
        migrations.AlterField(
            model_name='discount',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='image',
            field=models.ImageField(upload_to='discount/images/', verbose_name='Выберите изображение'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='title',
            field=models.CharField(help_text='Введите заголовок', max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_description',
            field=models.TextField(blank=True),
        ),
    ]