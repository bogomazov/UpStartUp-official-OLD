from django.conf.urls import include, patterns, url
from django.contrib import admin

from rest_framework import routers

from views import APIRoot
from userprofile.views import UserProfileViewSet

urlpatterns = patterns(
    '',
    # url(r'^api/v1/', include('startup.urls')),
    url(r'^api/v1/auth/', include('userprofile.urls')),
    url(r'^api/', APIRoot.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url('', include('social.apps.django_app.urls', namespace='social')), #specified in settings.py as LOGIN_URL etc.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', 'django.contrib.staticfiles.views.serve', kwargs={'path': 'index.html'}),
)