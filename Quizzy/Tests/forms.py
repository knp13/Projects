from django import forms
from django.forms import ModelForm
from .models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'text':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'option1':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'option2':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'option3':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'option4':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'answer':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'marks':forms.TextInput(attrs={'class':'textinputclass form-control'})
        }

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['text', 'option1', 'option2', 'option3', 'option4']
    # CHOICES = [('1', 'First'), ('2', 'Second')]
    # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['option1'].widget.attrs.update({'widget': 'forms.RadioSelect'})
    #     self.fields['option2'].widget.attrs.update(size='40')

# CHOICES = [('A','A'),('B','B'),('C','C'),('D','D')]
# class QuestionsForm(forms.Form):
#     choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    #text = forms.CharField(max_length=100)
    # option1 = forms.CharField(max_length=100)
    # option2 = forms.CharField(max_length=100)
    # option3 = forms.CharField(max_length=100)
    # option4 = forms.CharField(max_length=100)
