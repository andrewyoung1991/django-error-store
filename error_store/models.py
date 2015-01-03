import json

from django.db import models
from django.core.handlers.wsgi import WSGIRequest


class WSGIRequestField(models.TextField):
    """
    a database representation of a WSGIRequest object instance.
    """
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if isinstance(value, WSGIRequest):
            return value
        environ = json.loads(value)
        return WSGIRequest(environ)

    def get_prep_value(self, value):
        # save request object as a json string
        if value is None:
            return
        return json.dumps(value.environ, separators=(',', ': '),
                          cls=WSGIEnvironEncode)


class WSGIEnvironEncode(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, (str, dict, tuple, list)):
            return ''
        return json.JSONEncoder.default(self, obj)


class ServerError(models.Model):
    """a database representation of a server error, usefull for reproducing
    errors.
    """
    class Meta:
        ordering = ['-datetime']

    datetime = models.DateTimeField(auto_now=True)
    request = WSGIRequestField()

    def test_error(self, view_func, *args, **kwargs):
        """the main worker of the ServerError object. takes a view function and
        tests its response by passing in the failing WSGIRequest object.
        """
        return view_func(self.request, *args, **kwargs)
