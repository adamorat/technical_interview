from django.urls import path, include
from rest_framework.routers import DefaultRouter

from star_wars.films.views import FilmView, FilmApiView, FilmDetailView

router = DefaultRouter()
router.register(r'film', FilmApiView, base_name='film')

app_name = 'films'
urlpatterns = [
    path('api/', include(router.urls)),
    path('', view=FilmView.as_view(), name='index'),
    path('detail/<int:id>', FilmDetailView.as_view(), name='detail')
    # path('list/', )
]
