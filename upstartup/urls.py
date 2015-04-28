from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from constructor import views
from emailusernames.forms import EmailAuthenticationForm
import emailusernames

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upstartup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(
    #     r'^$', 'django.contrib.staticfiles.views.serve', kwargs={
    #         'path': 'index.html'}),
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^post/(?P<action>\w{0,50})/$', views.post, name='post'),
    url(r'^post/(?P<action>\w{0,50})/(?P<startup_id>\w{0,50})/$', views.post, name='question_answer'),
    # url(r'^edit-startup/(?P<startup_id>\w{0,50})/$', views.post, name='edit-startup'),
    url(r'^startup/(?P<startup_id>\w{0,50})/$', views.startup_profile, name='startup_profile'),
    url(r'^/develop/(?P<startup_id>\w{0,50})/$', views.develop, name='startup_profile'),
    url(r'^/develop/(?P<area>\w{0,50})/(?P<startup_id>\w{0,50})/$', views.develop_area, name='startup_profile'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
) + staticfiles_urlpatterns()
