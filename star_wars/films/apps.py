from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FilmsApp(AppConfig):
    name = 'star_wars.films'
    verbose_name = _("Películas")

    def ready(self):
        try:
            import star_wars.films.signals
        except ImportError:
            pass
