from django.conf import settings
from django.utils import translation


class QueryLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.LANGUAGE_CODE
        if (request.method == 'GET'
                and 'lang' in request.GET
                and request.GET['lang'] in [lang[0] for lang in settings.LANGUAGES]):
            language = request.GET['lang']
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = language

        response = self.get_response(request)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        return response
