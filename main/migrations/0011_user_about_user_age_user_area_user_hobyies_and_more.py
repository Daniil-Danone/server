# Generated by Django 4.2.2 on 2023-07-06 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_marks_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.CharField(blank=True, default='Не указано', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(blank=True, default='Не указано', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='area',
            field=models.CharField(blank=True, default='Не указано', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='hobyies',
            field=models.TextField(blank=True, default='Не указаны'),
        ),
        migrations.AddField(
            model_name='user',
            name='links',
            field=models.CharField(blank=True, default='Не указано', max_length=255),
        ),
    ]