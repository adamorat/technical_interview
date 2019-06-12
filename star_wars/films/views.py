# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from star_wars.characters.models import Character
from star_wars.films.models import Film
from star_wars.films.serializers import FilmSerializer


class FilmView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        kwargs.update({'characters': Character.objects.all()})
        return super().get(request, *args, **kwargs)


class SearchFilmFormView(LoginRequiredMixin, ListView):
    model = Film
    search_fields = ['title', ]


class FilmApiView(mixins.ListModelMixin, GenericViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['title']


class FilmDetailView(LoginRequiredMixin, TemplateView):
    template_name = "film_detail.html"
    model = Film

    def get(self, request, *args, **kwargs):
        film_id = kwargs.get('id')
        kwargs['film'] = self.model.objects.get(id=film_id)
        return super().get(request, *args, **kwargs)
