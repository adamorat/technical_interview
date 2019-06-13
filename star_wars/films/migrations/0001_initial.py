# Generated by Django 2.2.2 on 2019-06-08 18:04

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
from django.db.migrations import RunPython
from swapi import swapi


def get_films_data(apps, schema_editor):
    Film = apps.get_model('films', "Film")
    Character = apps.get_model('characters', 'Character')
    for film in swapi.get_all('films').iter():
        available_fields = Film._meta.get_fields()
        available_fields = [i.name for i in available_fields]
        if 'characters' not in available_fields:
            available_fields += ['characters']
        film_data = {i: getattr(film, i, None) for i in available_fields}
        urls = film_data.pop('characters', None)
        characters = Character.objects.filter(url__in=urls)
        film = Film.objects.create(**film_data)
        film.characters.set(characters)
        film.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255)),
                ('episode_id', models.IntegerField()),
                ('opening_crawl', models.TextField()),
                ('director', models.CharField(max_length=255)),
                ('producer', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('url', models.TextField()),
                ('characters', models.ManyToManyField(to='characters.Character')),
            ],
            options={
                'verbose_name': 'Película',
                'verbose_name_plural': 'Películas',
            },
        ),
        RunPython(get_films_data, RunPython.noop)
    ]