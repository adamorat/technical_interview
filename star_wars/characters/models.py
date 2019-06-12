# -*- coding: utf-8 -*-

from random import randint

from django.db import models
from django.db.models import CharField, TextField, ForeignKey, ImageField, Count
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

    class Meta:
        verbose_name = _("Personaje")
        verbose_name_plural = _("Personajes")

    @property
    def random_image(self):
        queryset = self.characterimage_set.all()
        count = queryset.count()
        random_index = randint(0, (count or 1) - 1)
        return queryset[random_index].image

    @property
    def description(self):
        pronoun = 'her' if self.gender in ['Female'] else ('his' if self.gender in ['Male'] else 'its')
        data = {**{'pronoun': pronoun, 'pronoun_c': pronoun.capitalize()}, **self.__dict__}
        description = "%(name)s was born in %(birth_year)s. %(pronoun_c)s eyes are %(eye_color)s and %(pronoun)s hair " \
                      "is %(hair_color)s. " \
                      "Height %(height)s & weight %(mass)s. Residence home: %(homeworld)s" % data
        return description


class CharacterImage(TimeStampedModel):
    character = ForeignKey(Character, on_delete=models.CASCADE)
    image = ImageField(upload_to='characters/uploaded', default='characters/default/default.jpg')

    class Meta:
        verbose_name = _("Personaje")
        verbose_name_plural = _("Personajes")
