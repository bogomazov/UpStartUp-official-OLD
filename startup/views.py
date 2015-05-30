from django.shortcuts import render
from django.http import HttpResponse
# from restful.urls import QUESTION_ANSWER_URL
from models import *

# Create your views here.

def show_startup_profile(request, startup_id=None):
    pass

def edit_answer(request):
    import json

    data_json = request.body
    data = json.loads(data_json)
    answer = Answer.objects.get(pk=data['pk'], founder=request.user.userprofile)
    if answer:
        answer.answer_content = data['value']
        answer.save()
        return HttpResponse()
    else:
        return HttpResponse(status=404)


def edit_startup_profile(request, startup_pk=None):
    if startup_pk == None:
        try:
            startup_pk = Startup.objects.filter(founder=request.user.userprofile)[0].pk
        except Startup.DoesNotExist:
            return HttpResponse(status=400)

    from upstartup.constants import get_context, STARTUP_PROFILE_JS, STARTUP_PROFILE_CSS

    context  = get_context(STARTUP_PROFILE_JS, STARTUP_PROFILE_CSS)
    question_answer_context = get_question_answer_context(startup_pk, request.user.userprofile)
    context.update(question_answer_context)
    context['question_answer_url'] = QUESTION_ANSWER_URL.format(startup_pk=startup_pk)
    context['startup_id'] = startup_pk
    return render(request, 'startup-profile.html', context)

def get_question_answer_context(startup_pk, userprofile):
    # if  startup_pk == None:
    #     startup = Startup.objects.filter(founder=userprofile)[0]
    # else:
    startup = Startup.objects.get(founder=userprofile, pk=startup_pk)
    question_translations = Question.get_questions_translation(userprofile.current_language)
    answers = Answer.get_answers(startup, userprofile.current_language)
    context = {}
    # context = {'startup_id': startup.pk}
    for question_translation in question_translations:
        question_type_name = question_translation.question.question_type.name
        if question_type_name == "Text":
            answer_pk = 0
            answer_text = ''
            for answer in answers:
                if answer.question == question_translation.question:
                    answer_pk = answer.pk
                    answer_text = answer.answer_text
            context[question_translation.question.question_nick] = \
            {
                'question_text': question_translation.question_text,
                'question_hint': question_translation.question_hint,
                'question_pk': question_translation.question.pk,
                'answer_pk': answer_pk,
                'answer_text': answer_text,
            }
        elif question_type_name == "Table":
            context[question_translation.question.question_nick] = \
            {
                'question_text': question_translation.question_text,
                'question_hint': question_translation.question_hint,
                'question_pk': question_translation.question.pk,
                'row': answer_text,
            }
        elif question_type_name == "Column":
            pass
        elif question_type_name == "Row":
            pass

    return context




