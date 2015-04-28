import json

from django.http import HttpResponse
from django.contrib.staticfiles.views import serve
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from login.linkedin import login_auth
from constructor.startup.post import edit_startup, new_startup

from constructor.login import linkedin


def login_view(request):
    if request.method == 'GET':
        if 'code' in request.GET.keys():
            user_profile = login_auth(request.GET['code'])
            auth_user = authenticate(username=user_profile.user.username, password="upstartup")
            if auth_user is not None:
                if auth_user.is_active:
                    login(request, auth_user)
                    return redirect('/')
        else:
            return serve(request, 'loginfail.html')
        return HttpResponse(str("lol"))
def logout_view(request):
    logout(request)

    return redirect('/')


def startup_profile(request, startup_id=None):
    from startup.views import show_questions, startup_profile
    from models import Startup

    if startup_id:
        return startup_profile(request, startup_id)

    startup = Startup.objects.filter(founder=request.user.userprofile)
    if len(startup) == 0:
        return show_questions(request)
    return redirect('/startup/{}/'.format(startup[0].id))

def develop(request, startup_id):
    pass

def develop_area(request, area, startup_id):
    pass



def post(request, action, startup_id=None):
    if request.method == 'POST':
        if request.user.is_authenticated():
            if startup_id:
                return edit_startup(request, startup_id)
            # if action == 'edit-answer':
            #     edit_startup(request)
            if action == 'startup':
                return new_startup(request)
    return HttpResponse(str("Hello!"))


def index(request):
    if request.user.is_authenticated():
        return startup_profile(request)
    else:
        return serve(request, 'index.html')



