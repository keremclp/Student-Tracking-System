# forms.py
from .models import AssignmentFile, Choice, UploadedSolution
from django import forms
from .models import Quiz, Question, Choice

# ASSIGNMENT VIA QUIZ


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


ChoiceFormSet = forms.inlineformset_factory(
    Question, Choice, fields=('text', 'is_correct'), extra=1, can_delete=False)

# ASSIGNMENT VIA UPLOADING FILE


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = AssignmentFile
        fields = ['title', 'deadline', 'description']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class UploadedSolutionForm(forms.ModelForm):
    class Meta:
        model = UploadedSolution
        fields = ['file']
