from django.contrib import admin
from models import *

# Register your models here.

class QuestionCategoryAdmin(admin.ModelAdmin):
    fields = ['question_category_title']


class OptionInline(admin.StackedInline):
    model = AnswerOption
    extra = 3
class OptionTranslationInline(admin.StackedInline):
    model = AnswerOptionTranslation
    extra = 3
class TranslationInline(admin.StackedInline):
    model = QuestionTranslation
    extra = 1
    #erase in production
    max_num = 1

class AnswerOptionAdmin(admin.ModelAdmin):
    inlines = [OptionTranslationInline]
class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [TranslationInline, OptionInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(QuestionTranslation)
admin.site.register(QuestionType)
admin.site.register(Startup)
admin.site.register(StartupMember)
admin.site.register(QuestionCategory, QuestionCategoryAdmin)
admin.site.register(PublicAccess)
admin.site.register(Answer)
admin.site.register(AnswerOption, AnswerOptionAdmin)
admin.site.register(StartupStage)
