from django.db import models
import datetime
# from django.contrib.auth.models import User
from userprofile.models import UserProfile, Language


# Create your models here.

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

    def __unicode__(self):
        return u"Options for question {}".format(self.question.question_nick)
    def get_translations(self, language_name='en'):
        language = Language.get_language(language_name)
        return AnswerOptionTranslation.objects.filter(language=language, question=self)

class AnswerOptionTranslation(models.Model):
    option = models.ForeignKey('AnswerOption')
    language = models.ForeignKey(Language)
    name = models.CharField(max_length=100, default='')

    def __unicode__(self):
       return u"Option {} to the question: {}".format(self.name, self.option.question.question_nick[:10])


class Question(models.Model):
    _questions_translation = {} #key language nick, value - questions

    question_nick = models.CharField(max_length=50, default="")
    question_category = models.ForeignKey(QuestionCategory, default=0)
    question_parent = models.ForeignKey('self', blank=True, null=True)
    question_type = models.ForeignKey(QuestionType, default=0)
    startup_stage = models.ForeignKey('StartupStage', default=0)
    def __unicode__(self):
       return u"""category: "{}" question: \"{}\"""".format(self.question_category.question_category_title, self.question_nick)

    # def get_answer_from_startup(self, startup):
    #     try:
    #         answer = Answer.objects.get(startup=startup, question=self)
    #         answer_translation = answer.get_answer_translation
    #         return Answer.objects.get(startup=startup, question=self)
    #     except:
    #         return None

    def get_questions_child(self):
        return Question.objects.filter(question_parent=self)

    @staticmethod
    def get_questions_translation(cls, language):
        return cls._questions_translation[language]

    @staticmethod
    def load_questions_translation(cls):
        for language in Language.objects.all():
            questions_translation = QuestionTranslation.objects.filter(language=language)
            cls._questions_translation[language] = questions_translation

class QuestionTranslation(models.Model):
    question = models.ForeignKey('Question', default=0)
    language = models.ForeignKey(Language, default=0)
    question_text = models.CharField(max_length=200)
    question_hint = models.CharField(max_length=200, default="", blank=True)



class StartupMember(models.Model):
    startup = models.ForeignKey('Startup', default=0)
    user = models.ForeignKey(UserProfile, blank=True)
    position = models.CharField(max_length=200, default='')

class StartupStage(models.Model):
    stage = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    def __unicode__(self):
       return u"{} with priority rate {}".format(self.stage, self.rate)

class Startup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    founder = models.ForeignKey(UserProfile)
    stage = models.ForeignKey('StartupStage', null=True)
    logo = models.ImageField(upload_to='startup/logo', null=True)
    profile_image = models.ImageField(upload_to='startup/logo', null=True)
    # location =
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class PublicAccess(models.Model):
    group_name = models.CharField(max_length=100)
    permission_rate = models.IntegerField(default=0)
    def __unicode__(self):
       return u"{} permission rate {}".format(self.group_name, self.permission_rate)

class TableAnswer(models.Model):
    answer = models.ForeignKey('Answer')
    question = models.ForeignKey('Question')
    row = models.IntegerField()

class Answer(models.Model):
    question = models.ForeignKey(Question)
    startup = models.ForeignKey(Startup)
    public_access = models.ForeignKey(PublicAccess, default=0)
    answer_option = models.ManyToManyField('AnswerOption', blank=True, default=[])
    language = models.ForeignKey(Language, default=0)
    answer_text = models.CharField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(UserProfile, default=0)

    @staticmethod
    def get_answers(startup, language):
        return Answer.objects.filter(startup=startup, language=language)


    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        self.startup.modified_at = self.modified_at
        # self.modified_by = user_modifier
        return super(Answer, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.answer_text[:20]


# class AnswerTranslation(models.Model):
#     answer = models.ForeignKey(Answer)
#

    # Create your models here.
