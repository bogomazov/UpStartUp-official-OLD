from django.contrib import admin
from constructor.models import *
# Register your models here.

class QuestionCategoryAdmin(admin.ModelAdmin):
    fields = ['question_category_title']

class OptionInline(admin.StackedInline):
    model = AnswerOption
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionType)
admin.site.register(Startup)
admin.site.register(StartupMember)
admin.site.register(QuestionCategory, QuestionCategoryAdmin)
# admin.site.register(QuestionOrder)
# admin.site.register(ParentChildQuestion)
admin.site.register(PublicAccess)
admin.site.register(Answer)
admin.site.register(AnswerOption)


