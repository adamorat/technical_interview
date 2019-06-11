from django.urls import reverse
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from star_wars.films.models import Film


class FilmSerializer(serializers.ModelSerializer):
    url = SerializerMethodField()

    class Meta:
        model = Film
        fields = ('id', 'title', 'url')
        read_only_fields = fields

    def get_url(self, obj):
        full_path = self.context['request'].build_absolute_uri(reverse('films:detail', args=(obj.id, )))
        return full_path
