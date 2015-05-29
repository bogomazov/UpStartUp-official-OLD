from rest_framework import renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from userprofile.views import UserProfileViewSet

class APIRoot(APIView):
    def get(self, request):
        # Assuming we have views named 'foo-view' and 'bar-view'
        # in our project's URLconf.
        return Response({
            'User Login': reverse('login', request=request),
            'User Logout': reverse('logout', request=request),
            'User Register': reverse('register', request=request),
            'Check username or email for uniqness': reverse('unique', request=request),
            'User List': reverse('userprofile-list', request=request),
            'User Get': reverse('userprofile-detail', request=request, kwargs={'pk': '9'}),
            # 'logout': reverse('LogoutView.as_view()', request=request)
        })