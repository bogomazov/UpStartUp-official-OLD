import urllib2
import json
from django.contrib.auth.models import User

LINKEDIN_API_KEY = '77h9bqu8q3dpv3'
LINKEDIN_SECRET_KEY = 'F3hVOuVTAlqc7LLW'
REDIRECT_URL = 'http://127.0.0.1:8000/login'
BODY_TEMPLATE = "grant_type=authorization_code&code={}&redirect_uri={}&client_id={}&client_secret={}"
HEADERS = {
                # 'Host:' 'www.upstartup.bogomazz.com'
                'Content-Type': 'application/x-www-form-urlencoded'
            }

REQUEST_TEMPLATE = "https://api.linkedin.com/v1/people/~:({})?format=json"
REQEST_FIELDS = [
                 'num-connections',
                 'picture-url',
                 'email-address',
                 'headline',
                 'location',
                 'industry',
                 'summary',
                 'first-name',
                 'last-name'
]


def get_access_token(code):
    body = BODY_TEMPLATE.format(code, REDIRECT_URL, LINKEDIN_API_KEY, LINKEDIN_SECRET_KEY)
    req = urllib2.Request('https://www.linkedin.com/uas/oauth2/accessToken', body, HEADERS)
    return urllib2.urlopen(req).read()

def get_data_linkedin(access_token):
    HEADER_AUTH = {
        # 'Host': 'www.upstartup.bogomazz.com',
        'Accept': "*/*",
        # "Accept-Encoding": "gzip, deflate",
        'Authorization': "Bearer {}".format(access_token),
        "User-Agent": "runscope/0.1",

    }
    req = urllib2.Request(REQUEST_TEMPLATE.format(",".join(REQEST_FIELDS)), None, HEADER_AUTH)
    response_json = urllib2.urlopen(req).read()
    data = json.loads(response_json)

    return data

def login_auth(linkedin_code):
    from ..models import UserProfile
    response_json = get_access_token(linkedin_code)
    response_dict = json.loads(response_json)
    data = get_data_linkedin(response_dict['access_token'])
    data['access_token'] = response_dict['access_token']
    data['expires_in'] = response_dict['expires_in']
    try:
        user = User.objects.get(email=data['emailAddress'])
        return user.userprofile
    except:
        return UserProfile.create_user(data)





