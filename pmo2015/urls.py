from django.conf.urls import include, url
from django.contrib import admin
from pmo2015.views import BaseInfoView, StallView, EventView, RegisterView, NewsView, QABookView


urlpatterns = [
    # Examples:
    url(r'^$', 'pmo2015.views.home', name='home'),

    url(r'^baseinfo/$', BaseInfoView.as_view(), name='baseinfo'),
    url(r'^baseinfo/(?P<sub>.+)/$', BaseInfoView.as_view(), name='baseinfo'),

    url(r'^stall/$', StallView.as_view(), name='stall'),
    url(r'^stall/(?P<sub>.+)/$', StallView.as_view(), name='stall'),

    url(r'^event/$', EventView.as_view(), name='event'),
    url(r'^event/(?P<sub>.+)/$', EventView.as_view(), name='event'),

    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/(?P<sub>.+)/$', RegisterView.as_view(), name='register'),

    url(r'^news/$', NewsView.as_view(), name='news'),

    url(r'^qabook/$', QABookView.as_view(), name='qabook'),
    url(r'^qabook/(?P<sub>.+)/$', QABookView.as_view(), name='qabook'),
    url(r'^qabook/(?P<sub>.+)/(?P<page>\d+)/$', QABookView.as_view(), name='qabook'),

    url(r'^test/$', 'pmo2015.views.test', name='test'),
]

