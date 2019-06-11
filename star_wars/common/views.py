from django.views.generic import RedirectView


class MainView(RedirectView):
    pattern_name = 'films:index'
