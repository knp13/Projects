from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from Tests.views import *

urlpatterns = [
    path('que_list/<int:id>', que_list, name="que_list"),
    path('topic_list/', topic_list, name='topic_list'),
    path('result/<int:id>/', result, name="result"),
    path('tests/<int:id>/', tests_given, name="tests_given"),
    #path('question_list/', question_list, name="question_list"),
    path('question_list/', staff_member_required(Question_List.as_view()), name="question_list"),
    path('add_question/', add_question, name="add_question"),
    path('edit_question/<int:id>/', edit_question, name="edit_question"),
    path('delete_question/<int:id>/', delete_question, name="delete_question"),
]
