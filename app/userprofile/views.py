import json

from django.contrib.auth import authenticate, login, logout

from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response

from rest_framework import renderers

from models import UserProfile
from serializers import UserProfileSerializer
from permissions import IsUserOwner

from models import UserProfile



class UserProfileViewSet(viewsets.ModelViewSet):
    # lookup_field = 'username'
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsUserOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            UserProfile.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

class LoginView(views.APIView):
    """
    Login user
    POST request

{
    <br>"login_type": may be "email" or "username",
    <br>"login": "bender",
    <br>"password: "buzz",<br>
}

    """
    def post(self, request, format=None):
        data = json.loads(request.body)

        login_type = data.get('login_type', None)
        user_login = data.get('login', None)
        user_password = data.get('password', None)

        if login_type == 'email':
            user = authenticate(email=user_login, password=user_password)
        elif login_type == 'username':
            user = authenticate(username=user_login, password=user_password)


        if user is not None:
            if user.is_active:
                login(request, user)

                serialized = UserProfileSerializer(user)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)

class RegisterView(views.APIView):
    """
    Register new user and logs in
    POST request

{
    <br>"email": may be "email" or "username", [check for being unique][ref].
    <br>"username": "bender",                  [check for being unique][ref]
    <br>"password: "buzz",<br>
} <br>
If created: Response is HTTP_201_CREATED <br>
else:       Response is HTTP_400_BAD_REQUEST <br>

[ref]: /api/v1/auth/is-unique/
    """
    def post(self, request, format=None):
        data = json.loads(request.body)

        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            login(request, user)
            return Response({}, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad Request',
            'message': 'Wrong parameters'
        }, status=status.HTTP_400_BAD_REQUEST)

class CheckUniqueView(views.APIView):
    """
    Register new user
    POST request

{
    <br>"login_type": may be "email" or "username",
    <br>"field": "some data to check for being unique",
<br>}
<br>if unique: Response status is 200
<br>else:      Response status is 400
    """
    def post(self, request, format=None):
        data = json.loads(request.body)

        login_type = data.get("login_type", None)
        field = data.get("field", None)

        try:
            if login_type == "email":
                UserProfile.objects.get(email=field)
            elif login_type == "username":
                UserProfile.objects.get(username=field)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response({}, status=status.HTTP_200_OK)


