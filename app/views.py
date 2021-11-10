from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


questions = [
    {
        "id": i,
        "title": f"Title {i}",
        "text": f"This is text for {i} question."
        #"number": i,
    } for i in range(20)
]

answers = [
    {
        "title": f"Title {i}",
        "id": f"{i}",
        "text": f"I know! You just should do {i+1}",
    } for i in range(20)
]

def paginate(objects_list, request, per_page=5):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    some_objects_list = paginator.get_page(page)
    return page, some_objects_list

def index(request):
    pagination = paginate(questions, request, 5)
    return render(request, "index.html", {'current_page': pagination[0], 'questions':pagination[1]})

def ask(request):
    return render(request, "ask.html",{})

def login(request):
    return render(request, "login.html",{})

def signup(request):
    return render(request, "signup.html",{})

def tag(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "tag.html", {'questions': content})

def user_settings(request):
    return render(request, "user_settings.html",{})

def hot(request):
    pagination = paginate(questions, request , 5)
    return render(request, "hot.html", {'current_page': pagination[0], 'questions':pagination[1]})

#def question(request, number):
#    return render(request, "question.html", {questions[number]})
#def question(request, number="1"):
#    return render(request, "question.html", {questions[number]})

def question(request, number):
    question = questions[number]
    pagination = paginate(questions, request, 5)
    return render(request, "index.html", {'current_page': pagination[0], 'questions' : pagination[1], "question" : question})

def tag(request, tag):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "tag.html", {'questions': content, 'tag_name': tag})
