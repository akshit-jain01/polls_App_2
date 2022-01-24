from ntpath import join
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404

def index(request):
    question_list = Question.objects.order_by('pub_date')[:5]
    # output = ", ".join([q.question for q in question_list])
    context = {'question_list':question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response  = "You are looking at the results of the question %s." 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting for question %s." % question_id)

    


