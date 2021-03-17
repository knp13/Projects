from django.shortcuts import render, redirect
from .models import *
from Users.models import *
from .forms import QuestionForm
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator

# Create your views here.
user_answer_list = []
answer_list = []
mark_list = []
topicname = ""
answers = Question.objects.all()
for i in answers:
    answer_list.append(i.related_answer)

def home(request):
    return render(request, 'index.html', {})

def topic_list(request):
    topic = Topic.objects.all()
    users = User.objects.all()
    return render(request, 'topic.html', {'topic':topic, 'users':users})

@login_required
def tests_given(request, id):
    tgiven = TestsGiven.objects.filter(user=id)
    return render(request, 'tests.html', {'tgiven':tgiven})

@login_required
def que_list(request, id):
    que = Question.objects.filter(topic=id)
    topicname = que[0].topic
    qcount = Question.objects.filter(topic=id).count()
    request.session['result'] = 0
    if request.method == 'POST':
        newvar=1
        for i in range(len(que)):
            user_answer_list.append(request.POST.get('question'+str(newvar)))
            mark_list.append(que[i].marks)
            newvar+=1
        t = TestsGiven.objects.create(user=request.user, topic=topicname, completed=True)
        for i in range(len(user_answer_list)):
            if user_answer_list[i] in answer_list:
                t.score += mark_list[i]
        for i in mark_list:
            t.total_score += i
        #request.session['result'] = t.score
        t.save()
        user_answer_list.clear()
        mark_list.clear()
        return redirect("result", id=t.id)
    return render(request,'question_list.html', {'que':que, 'qcount':qcount, 'topicname':topicname, 'marks':mark_list})

@login_required
def result(request, id):
    message = ""
    tgiven = TestsGiven.objects.get(id=id)
    topicname = tgiven.topic.name
    passing = tgiven.total_score//2
    if tgiven.score >= (tgiven.total_score//2):
        message = "Congratulations ! You Passed the Test."
    else:
        message = "Oops ! You can try again to score better."
    context = {'t':tgiven, 'message':message, 'passing':passing}
    return render(request,'result.html', context)


def contact(request):
    return render(request, 'contact.html', {})

class Question_List(ListView):
    model = Question
    template_name = 'questions.html'
    context_object_name = 'questions'
    ordering = ['-id']
    paginate_by = 5

@staff_member_required
def add_question(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic_list')
    return render(request, 'forms.html', {'form':form})

@staff_member_required
def edit_question(request, id):
    question = Question.objects.get(id=id)
    form = QuestionForm(instance=question)
    return render(request, 'forms.html', {'form':form})

@staff_member_required
def delete_question(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return render(request, 'questions.html')
