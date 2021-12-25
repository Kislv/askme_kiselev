import random
from random import sample, choice
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from app.models import *

list_all_tags = ['Perl', 'Python', 'TechnoPark', 'MYSQL', 'django', 'Mail.ru', 'Voloshin', 'Firefox']

def paginate(objects_list, request, per_page=5):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    some_objects_list = paginator.get_page(page)
    #return page, some_objects_list
    return paginator.get_page(page)


def index(request):
    question = paginate(Question.objects.newest(), request)
    return render(request, 'index.html', {'questions': question})

def hot(request):
    question = paginate(Question.objects.most_popular(), request)
    return render(request, 'index.html', {'questions': question})

def ask(request):
    return render(request, "ask.html",{})

def login(request):
    return render(request, "login.html",{})


def signup(request):
    return render(request, "signup.html",{})


def user_settings(request):
    return render(request, "user_settings.html",{})

def question(request, number):
    question = get_object_or_404(Question, id=number)
    answers = question.answers.hot()
    return render(request, "question.html", {"question": question, "answers": answers,
                                             "tags": sample(list_all_tags, 2)})


def tag(request, tag):
    question = paginate(Tag.objects.question_by_tag(tag), request)
    return render(request, 'tag.html', {'questions': question, "tag": tag})

