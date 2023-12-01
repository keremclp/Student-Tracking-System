# forms.py
from .models import Choice
from django import forms
from .models import Quiz, Question, Choice


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'text',
            'quiz'
        ]


ChoiceFormSet = forms.inlineformset_factory(Question, Choice, fields=('text', 'is_correct'), extra=1, can_delete=False)
