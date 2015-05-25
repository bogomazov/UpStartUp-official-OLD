from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User as AUTH_USER
import datetime

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        user = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)

        user.is_admin = True

        user.save()

        return user


class UserProfile(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    tagline = models.CharField(max_length=140, blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
    @property
    def is_staff(self):
        return self.is_admin
    @property
    def is_superuser(self):
        return self.is_admin
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class UserType(models.Model):
    name =  models.CharField(max_length=50, default="")

    def __unicode__(self):
        return self.name

# class UserProfile(models.Model):
#     user = models.OneToOneField(AUTH_USER)
#     type = models.ForeignKey(UserType)
#     # access_token = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100, default="")
#     last_name = models.CharField(max_length=100, default="")
#     avatar = models.ImageField(upload_to='static/files/user/avatar', default="")
#     avatar_url = models.CharField(max_length=100, default="")
#     country = models.CharField(max_length=100, default="")
#     headline = models.CharField(max_length=100, default="")
#     industry = models.CharField(max_length=100, default="")
#     summary = models.CharField(max_length=500, default="")
#     expires_in = models.CharField(max_length=100, default="")
#     current_language = models.ForeignKey('Language', default=0)
#
#     created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.today())
#     updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.today())
#
#
#     @classmethod
#     def get_expires_date(cls, expires_in_seconds):
#         import datetime
#         current_date = datetime.datetime.now()
#         expired_date = datetime.timedelta(seconds=expires_in_seconds) + current_date
#
#         return expired_date.strftime("%Y-%m-%d %H:%M:%S")
#
#     @classmethod
#     def create_user(cls, data):
#         user = User.objects.create_user(username=data['access_token'], email=data['emailAddress'], password='upstartup')
#         user_profile = cls(user = user)
#         user_profile.first_name = data['firstName']
#         user_profile.last_name = data['lastName']
#         user_profile.avatar_url = data['pictureUrl']
#         user_profile.country = data['location']['name']
#         user_profile.industry = data['industry']
#         user_profile.headline = data['headline']
#         user_profile.summary = data['summary']
#         user_profile.expires_in = cls.get_expires_date(data['expires_in'])
#
#         user.save()
#         user_profile.save()
#
#         return user_profile

#ua, ru, eng etc.
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
       return u"{}".format(self.name)