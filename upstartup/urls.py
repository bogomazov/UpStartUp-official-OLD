from django.conf.urls import include, patterns, url
from views import IndexView

from userprofile.views import LoginView, LogoutView
from settings import STATIC_ROOT

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include('startup.urls')),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url(
        r'^.*$', 'django.contrib.staticfiles.views.serve', kwargs={'path': 'index.html'}),
)