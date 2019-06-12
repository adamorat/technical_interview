import logging
from urllib.parse import urlparse

from django.conf import settings
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from star_wars.url_history.models import UrlHistory

log = logging.getLogger(__file__)


class URLHistoryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            visited_url = request.get_full_path()
            if not [avoid_url for avoid_url in settings.AVOID_HISTORY_URLS
                    if reverse(avoid_url) == urlparse(visited_url).path]:
                try:
                    UrlHistory.objects.create(user=request.user, url=visited_url)
                except Exception as e:
                    log.warning(str(e))



