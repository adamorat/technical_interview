# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from star_wars.url_history.models import UrlHistory


class UrlHistoryView(LoginRequiredMixin, ListView):
    queryset = UrlHistory.objects.all()
    template_name = 'web_history.html'

    def get_queryset(self):
        self.queryset = self.queryset.filter(user=self.request.user)
        return super().get_queryset()
