from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'Quizzy Admin'

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'marks')
    list_filter = ['topic']

admin.site.register(Question, QuestionAdmin)

class TestsGivenAdmin(admin.ModelAdmin):
    list_display = ['score']

admin.site.register(TestsGiven)

admin.site.register(Answer)

admin.site.register(Topic)
