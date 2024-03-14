# Import necessary modules and classes
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

# Import models from the current app
from .models import Question, Choice

# View function to display a list of the latest questions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# View function to display details of a specific question
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, 'polls/detail.html', {'question': question})

# View function to display results for a specific question
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# View function to handle user votes for a specific question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You did not select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
# Import necessary modules and classes
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

# Import models from the current app
from .models import Question, Choice

def index(request):
    """
    View function to display a list of the latest questions.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """
    View function to display details of a specific question.

    Args:
        request: HttpRequest object.
        question_id: ID of the question to display.

    Returns:
        HttpResponse object.
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    View function to display results for a specific question.

    Args:
        request: HttpRequest object.
        question_id: ID of the question to display results for.

    Returns:
        HttpResponse object.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    """
    View function to handle user votes for a specific question.

    Args:
        request: HttpRequest object.
        question_id: ID of the question to vote on.

    Returns:
        HttpResponseRedirect object.
    """
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You did not select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
