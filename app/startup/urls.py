
__author__ = 'andrey'

from django.conf.urls import include, patterns, url
from userprofile.views import StartupViewSet

startup_list = StartupViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
startup_detail = StartupViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^startups/$', startup_list, name='startup-list'),
    url(r'^startup/(?P<pk>\w+)/', startup_detail, name='startup-detail'),
)