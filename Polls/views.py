from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question,Choice


# Create your views here.


def Index(requests):

    qstobj=Question.objects.all()

    return render(requests, 'Polls/Index.html',{'qst':qstobj})


def showchoices(request, questions_id):


    qstobj=Question.objects.get(pk=questions_id)

    return render(request, 'Polls/Choices.html',{'choice':qstobj})

def voted(request,questions_id):
    if request.method=="POST":
        qstobj=Question.objects.get(pk=questions_id)
        try:
            choiceobj=get_object_or_404(Choice,pk=request.POST['choice'])
        except:
            return HttpResponse("Please select a option")
        else:
            choiceobj.votes+=1
            choiceobj.save()
            return render(request,'Polls/Choices.html',{'choice':qstobj})
    return render(request, 'Polls/Choices.html')        
