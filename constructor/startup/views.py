# coding: utf-8

from ..models import Question, QuestionCategory, AnswerOption, Startup, Answer
from CONSTANTS import ADDITIONAL_FILES_CSS, ADDITIONAL_FILES_JS, STARTUP_PROFILE_CSS, STARTUP_PROFILE_JS, TEXT_TYPES
from django.shortcuts import render
from django.template import RequestContext, Template
from django.http import HttpResponse


def standard_processor(request):
    if hasattr(request.user, 'userprofile'):
        return {'username': request.user.userprofile.first_name,
                'avatar_url': request.user.userprofile.avatar_url,
                'additional_files_js': ADDITIONAL_FILES_JS,
                'additional_files_css': ADDITIONAL_FILES_CSS}
    return {}

def show_questions(request):
    question_category = QuestionCategory.objects.get(question_category_title=("Общие"))
    questions = Question.objects.filter(question_category=question_category).order_by('question_order')
    context = {
        'question_entries': questions,
        # 'username': request.user.userprofile.first_name,
        'options': {},
        # 'avatar_url': request.user.userprofile.avatar_url
    }
    for question in questions:
        if question.question_type.name == 'Button Menu':
            context['options'].update({ question.id: AnswerOption.objects.filter(question=question) })

    return render(request, 'question.html', context)

def get_question_answer_list(startup):
    questions = Question.objects.all().order_by('question_order')
    # print(questions)
    answers = []

    for question in questions:
        try:
            answers.append(Answer.objects.get(startup=startup, question=question))
        except:
            answers.append(None)
    # print(answers)
    # print(questions)
    return zip(questions, answers)

# def construct_table_context(question):
#     questions_child = question.get_questions_child()
#
#     for question in questions_child:
#         if question.question_type == "table":
#             return construct_table_context(question)
#
#     return {}


def get_profile_context(startup):
    # startup_name_question = Question.objects.get(question_order=1)
    # startup_name_answer = Answer.objects.get(startup=startup, question=startup_name_question)

    context = {
    # 'startup_name': startup_name_answer.answer_text,
    # 'startup_id': startup.id,
    'additional_files_js': ADDITIONAL_FILES_JS + STARTUP_PROFILE_JS,
    'additional_files_css': ADDITIONAL_FILES_CSS + STARTUP_PROFILE_CSS,
    'url_post': '/post/edit-answer/{}'.format(startup.id),
    # 'question_answer': get_question_answer_list(startup)

    }

    for question, answer in get_question_answer_list(startup):
        if question.question_type != "table":
            context[question.question_name] = { 'question': question, 'answer': answer }
        # else:
        #     questions_child = question.get_questions_child()
        #
        #     if questions_child.question_type == "table":
        #
        #     for question_child in
        #     context[question.question_name] = {  }

    return context


def startup_profile(request, startup_id):
    startup = Startup.objects.get(id=startup_id)

    context  = get_profile_context(startup)
    print(context)
    return render(request, 'startup-profile.html', context)
    # return HttpResponse(str("Hello!"))