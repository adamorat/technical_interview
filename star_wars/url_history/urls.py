from django.urls import path

from star_wars.url_history.views import UrlHistoryView


app_name = 'web_history'
urlpatterns = [
    path('list/', UrlHistoryView.as_view(), name='list')
]
