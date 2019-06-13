# Generated by Django 2.2.2 on 2019-06-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_characterimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characterimage',
            options={'verbose_name': 'Image de Personaje', 'verbose_name_plural': 'Image de Personajes'},
        ),
        migrations.RemoveField(
            model_name='characterimage',
            name='character',
        ),
        migrations.AddField(
            model_name='character',
            name='character_image',
            field=models.ManyToManyField(blank=True, to='characters.CharacterImage'),
        ),
    ]
