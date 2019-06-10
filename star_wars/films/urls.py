from django.urls import path

from star_wars.films.views import FilmView

app_name = 'films'
urlpatterns = [
    path('', view=FilmView.as_view(), name='index')
]
