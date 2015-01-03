django-error-store
==================

store django request objects for debugging / recreating server errors

install
-------
`$ pip install git+https://github.com/andrewyoung1991/django-error-store.git`

usage
-----
first add django-error-store to your installed apps and middleware
```python
INSTALLED_APPS = (
  ...,
  error_store
)

MIDDLEWARE_CLASSES = (
  ...,
  error_store.middleware.CaptureRequestErrors
)
```
make sure the middleware is at the bottom of the middleware stack.

now if you syncdb, or migrate `error_store` a single table will be created in the database called `ServerError`.

###ServerError

the `ServerError` object contains two fields, namely datetime and a request. 
request is a serialized instance of the `django.core.handlers.WSGIRequest` object. With this object you can now debug any
server errors locally.

```python
>>> from error_store.models import ServerError
>>> from myapp.views import myviewfunc
>>> errors = ServerError.objects.all()  # returns all ServerErrors in reverse chronological order
>>> response = myviewfunc(errors[0].request, *args, **kwargs)
>>> response
<django.http.response.HttpResponse object ...>
>>> response.status_code
500
```
you can now debug against this request object rather than attempting to reproduce the error locally.

TODO
----
* add error_class field to ServerError
* add error_store view/template for altering request data
* store datetime type based on user settings
* documentation for easy usage in unit tests
