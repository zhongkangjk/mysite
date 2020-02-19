from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404

from .models import Question



def index(request):
    lastet_question_list = Question.objects.order_by('-pub_date')[:1]
    context = {
        'latest_question_list':lastet_question_list,
    }
    return render(request,'polls/index.html',context)

# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("这个问题没有找到")
#     context = {
#         'question': question,
#     }
#     return render(request,'polls/detail.html',context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

