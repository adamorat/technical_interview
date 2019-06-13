from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class CharactersApp(AppConfig):
    name = 'star_wars.characters'
    verbose_name = _("Users")

    def ready(self):
        try:
            import star_wars.characters.signals
        except ImportError:
            pass
