from django.conf.urls import patterns, include, url

urlpatterns = patterns('resources.views',
    url(r'^$', 'index'),
)
