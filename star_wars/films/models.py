from django.db.models import CharField, IntegerField, TextField, DateField, ManyToManyField, ImageField
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from star_wars.characters.models import Character


class Film(TimeStampedModel):
    title = CharField(max_length=255)
    episode_id = IntegerField()
    opening_crawl = TextField()
    director = CharField(max_length=255)
    producer = CharField(max_length=255)
    release_date = DateField()
    characters = ManyToManyField(Character)
    url = TextField()
    image = ImageField(default='films/default/default.jpg', upload_to='films/uploaded')

    class Meta:
        verbose_name = _("Película")
        verbose_name_plural = _("Películas")
