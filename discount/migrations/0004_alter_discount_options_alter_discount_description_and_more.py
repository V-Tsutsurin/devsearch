# Generated by Django 4.2b1 on 2023-04-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0003_alter_discount_options_alter_slider_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': 'Скидку', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.AlterField(
            model_name='discount',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider',
            field=models.ImageField(upload_to='slider/images/', verbose_name='Выберите картинку'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_description',
            field=models.TextField(blank=True, verbose_name='Введите описание'),
        ),
    ]