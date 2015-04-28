# -*- coding: utf-8 -*-

# Create your models here.

from django.db import models
from django.contrib.auth.models import User



class QuestionCategory(models.Model):
    question_category_title = models.CharField(max_length=100)
    def __unicode__(self):
       return self.question_category_title

# class QuestionOrder(models.Model):
#     question = models.ForeignKey('Question')
#     order = models.IntegerField(default=0)
#     def __unicode__(self):
#        return u"#{} category: {} question: {}".format(self.order, self.question.question_category.question_category_title, self.question.question_text)

class QuestionType(models.Model):
    name = models.CharField(max_length=100, default='')
    def __unicode__(self):
       return self.name

class AnswerOption(models.Model):
    question = models.ForeignKey('Question')
    option = models.CharField(max_length=100, default='')
    def __unicode__(self):
       return u"Option {} to the question: {}".format(self.option, self.question.question_text[:10])

class Question(models.Model):
    question_category = models.ForeignKey(QuestionCategory, default=0)
    # question_parent = models.ForeignKey('self', blank=True, null=True)
    question_text = models.CharField(max_length=200)
    question_name = models.CharField(max_length=200, default="")
    question_type = models.ForeignKey(QuestionType, default=0)
    question_hint = models.CharField(max_length=200, default="", blank=True)
    is_optional = models.BooleanField(default=False)
    question_order = models.IntegerField(default=0)
    def __unicode__(self):
       return u"""category: "{}" question: \"{}\"""".format(self.question_category.question_category_title, self.question_text)
    def get_answer_from_startup(self, startup):
        try:
            return Answer.objects.get(startup=startup, question=self)
        except:
            return None
    def get_questions_child(self):
        return Question.objects.filter(question_parent=self)


# class ParentChildQuestion(models.Model):
#     parent = models.ForeignKey(Question, related_name="question_parent")
#     child = models.ForeignKey(Question,  related_name="question_child")
#
#     def __unicode__(self):
#        return u"parent: {} question: {}".format(self.parent.question_text[:10], self.child.question_text[:10])


class StartupMember(models.Model):
    user = models.ForeignKey('UserProfile', blank=True)
    member_position = models.CharField(max_length=100)

class Startup(models.Model):
    founder = models.ForeignKey('UserProfile')
    co_founder = models.ManyToManyField(StartupMember, blank=True)

class PublicAccess(models.Model):
    group_name = models.CharField(max_length=100)
    permission_rate = models.IntegerField(default=0)
    def __unicode__(self):
       return u"{} permission rate {}".format(self.group_name, self.permission_rate)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    startup = models.ForeignKey(Startup)
    user = models.ForeignKey(User)
    answer_text = models.CharField(max_length=500)
    public_access = models.ForeignKey(PublicAccess, default=0)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # access_token = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    avatar_url = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")
    headline = models.CharField(max_length=100, default="")
    industry = models.CharField(max_length=100, default="")
    summary = models.CharField(max_length=500, default="")
    expires_in = models.CharField(max_length=100, default="")


    @classmethod
    def get_expires_date(cls, expires_in_seconds):
        import datetime
        current_date = datetime.datetime.now()
        expired_date = datetime.timedelta(seconds=expires_in_seconds) + current_date

        return expired_date.strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    def create_user(cls, data):
        user = User.objects.create_user(username=data['access_token'], email=data['emailAddress'], password='upstartup')
        user_profile = cls(user = user)
        user_profile.first_name = data['firstName']
        user_profile.last_name = data['lastName']
        user_profile.avatar_url = data['pictureUrl']
        user_profile.country = data['location']['name']
        user_profile.industry = data['industry']
        user_profile.headline = data['headline']
        user_profile.summary = data['summary']
        user_profile.expires_in = cls.get_expires_date(data['expires_in'])

        user.save()
        user_profile.save()

        return user_profile








