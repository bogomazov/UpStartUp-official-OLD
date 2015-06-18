__author__ = 'andrey'

from django.conf.urls import include, patterns, url
from app.userprofile.views import LoginView, LogoutView, RegisterView, CheckUniqueView, UserProfileViewSet

userprofile_list = UserProfileViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
userprofile_detail = UserProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^is-unique/$', CheckUniqueView.as_view(), name='unique'),
    url(r'^users/$', userprofile_list, name='userprofile-list'),
    url(r'^user/(?P<pk>\w+)/', userprofile_detail, name='userprofile-detail'),
)