from django.conf.urls import patterns, url


urlpatterns = patterns(
    'error_store.views',
    url(r'^$', 'test', name='test'),
)
