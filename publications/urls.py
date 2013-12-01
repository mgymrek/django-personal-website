from django.conf.urls import patterns, include, url

urlpatterns = patterns('publications.views',
    url(r'^$', 'index'),
    url(r'^article/(?P<pub_id>\d+)/$', 'article'),
)
