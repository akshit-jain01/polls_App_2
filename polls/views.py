from ntpath import join
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse

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
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detial.html', {
            'question':question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    


