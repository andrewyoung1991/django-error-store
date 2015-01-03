from models import ServerError


class CaptureRequestErrors(object):
    """dead simple response middleware that should be placed at the bottom of
    the middlware stack. simply captures and serializes server errors for
    testing/debugging later on.
    """
    def process_response(self, request, response):
        if getattr(response, "status_code", 0) >= 500:
            ServerError.objects.create(request=request)
        return response
