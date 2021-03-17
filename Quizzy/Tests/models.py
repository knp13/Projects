from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Topic(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TestsGiven(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=1)
    score = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    answer_given = models.CharField(max_length=100)
    # questions = models.ManyToOneField(Question, on_delete=models.CASCADE, default=1)
    # attempts = models.IntegerField(default=0)

    def __str__(self):
        if self.name == "":
            return self.topic.name+ " -\t" + str(self.id)
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100, blank=True, null=True)
    option2 = models.CharField(max_length=100, blank=True, null=True)
    option3 = models.CharField(max_length=100, blank=True, null=True)
    option4 = models.CharField(max_length=100, blank=True, null=True)
    marks = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=1)
    related_answer = models.CharField(max_length=100, blank=True, null=True)
    # score = models.IntegerField(default=0)
    # test = models.ForeignKey(TestsGiven, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.text

    def calculate_score(self):
        pass

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, default=1)
    user_selected_answer = models.CharField(max_length=100)
    right_answer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user_selected_answer
