# Generated by Django 4.1.1 on 2022-10-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(default='Опубликовано', max_length=20, verbose_name='Статус'),
        ),
    ]