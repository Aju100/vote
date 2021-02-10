from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone

def home(request):
    latest_question = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_question': latest_question
    }
    return render(request,'vote/index.html',context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        context = {
            'question':question,
            'error_message': "You didn't select a choice",
        }
        return render(request,'vote/detail.html',context)
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('vote:results', args=(question.id,)))

class DetailView(generic.DetailView):
    model = Question
    template_name = "vote/detail.html"


    def get_queryset(self):
        # Excludes any questions that aren't published yet.     
        return Question.objects.filter(pub_date__lte=timezone.now())
        

class ResultView(generic.DetailView):
    model = Question
    template_name = "vote/results.html"
