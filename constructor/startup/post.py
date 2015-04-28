# coding: utf-8
from ..models import Question, Answer, Startup, PublicAccess
from django.contrib import messages
from django.shortcuts import redirect
import json
from django.http import HttpResponse


def edit_startup(request, startup_id):
    json, user = request.body, request.user

    print(json)

    question = Question.objects.get(pk=json['pk'])
    startup = Startup.objects.get(pk=startup_id)
    # public_access = PublicAccess.objects.get(pk=query_dict['public-access'])
    answer = Answer.objects.get(startup=startup, user=request.user, question=question)
    answer.answer_text = json.value
    answer.save()
    # messages.info(request, "Thanks for registering. Please login to continue.")
    return HttpResponse('')

def new_startup(request):
    query_dict, user = request.POST, request.user

    answer_data = {key.replace("question[", "").replace("]", ""): value for key, value in query_dict.items() if 'question' in key}
    startup = Startup(founder=user.userprofile)
    startup.save()

    public_access = PublicAccess.objects.get(group_name="Доступ всем")
    #Create all answers
    for question in Question.objects.all():
        answer = Answer(question=question, startup=startup, user=user, answer_text="", public_access=public_access)
        answer.save()

    for question_id, value in answer_data.items():
        question = Question.objects.get(pk=question_id)
        # public_access = PublicAccess.objects.get(group_name="Доступ всем")
        answer = Answer.objects.get(startup=startup, question=question)
        answer.answer_text = value
        answer.save()

    # messages.info(request, "Thanks for registering. Please login to continue.")
    return redirect('/startup/'+str(startup.id))