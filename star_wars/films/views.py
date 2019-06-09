import itertools

from django.views.generic import TemplateView, FormView
from swapi import swapi

from star_wars.characters.models import Character
from star_wars.films.forms import SearchFilmForm


class FilmView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        kwargs.update({'characters': Character.objects.all()})
        return super().get(request, *args, **kwargs)


class SearchFilmFormView(FormView):
    form_class = SearchFilmForm

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """TODO: define correct film URL"""
        self.success_url = ''
        return super().form_valid(form)
