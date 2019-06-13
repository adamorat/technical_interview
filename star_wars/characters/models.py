# -*- coding: utf-8 -*-

from random import randint

from django.db.models import CharField, TextField, ImageField, ManyToManyField
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


GENDER_CHOICES = (
    ('Male', _("Hombre")),
    ('Female', _('Mujer')),
    ('unknown', _("Desconocido")),
    ('n/a', _("N/A"))
)


class Character(TimeStampedModel):
    name = CharField(max_length=255)
    birth_year = CharField(max_length=255)
    eye_color = CharField(max_length=255)
    gender = CharField(max_length=255, choices=GENDER_CHOICES)
    hair_color = CharField(max_length=255)
    height = CharField(max_length=255)
    mass = CharField(max_length=255)
    skin_color = CharField(max_length=255)
    homeworld = CharField(max_length=255)
    url = TextField()
    character_image = ManyToManyField('CharacterImage', blank=True)

    class Meta:
        verbose_name = _("Personaje")
        verbose_name_plural = _("Personajes")

    @property
    def random_image(self):
        queryset = self.character_image.all()
        count = queryset.count()
        random_index = randint(0, (count or 1) - 1)
        try:
            return queryset[random_index].image
        except IndexError:
            return None

    @property
    def description(self):
        pronoun = 'her' if self.gender in ['Female'] else ('his' if self.gender in ['Male'] else 'its')
        data = {**{'pronoun': pronoun, 'pronoun_c': pronoun.capitalize()}, **self.__dict__}
        description = "%(name)s was born in %(birth_year)s. %(pronoun_c)s eyes are %(eye_color)s and %(pronoun)s hair " \
                      "is %(hair_color)s. " \
                      "Height %(height)s & weight %(mass)s. Residence home: %(homeworld)s" % data
        return description


class CharacterImage(TimeStampedModel):
    image = ImageField(upload_to='characters/uploaded', default='characters/default/default.jpg')

    class Meta:
        verbose_name = _("Image de Personaje")
        verbose_name_plural = _("Image de Personajes")
