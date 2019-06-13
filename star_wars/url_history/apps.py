# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class URLHistoryApp(AppConfig):
    name = 'star_wars.url_history'
    verbose_name = _("Histórico de URLs")
