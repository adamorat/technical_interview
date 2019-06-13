from django.forms import forms


class SearchFilmForm(forms.Form):
    class Meta:
        fields = ("search", )
