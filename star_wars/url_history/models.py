# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models import ForeignKey, URLField
from model_utils.models import TimeStampedModel

User = get_user_model()


class UrlHistory(TimeStampedModel):
    user = ForeignKey(User, on_delete=models.CASCADE)
    url = URLField(max_length=255)

    class Meta:
        verbose_name = _("Histórico de URL visitada")
        verbose_name_plural = _("Histórico de URLs visitadas")
