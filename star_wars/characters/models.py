from django.db.models import CharField, TextField
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
