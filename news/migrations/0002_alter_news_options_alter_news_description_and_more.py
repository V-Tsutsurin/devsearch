# Generated by Django 4.2b1 on 2023-04-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(verbose_name='Введите текст новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news/images/', verbose_name='Выберите картинку'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Введите заголовок'),
        ),
    ]
