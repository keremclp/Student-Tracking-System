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


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text', 'is_correct']


ChoiceFormSet = forms.inlineformset_factory(
    Question,
    Choice,
    form=ChoiceForm,
    extra=2,  # Number of extra choice forms to display
    min_num=2,  # Minimum number of choices required
    validate_min=True,
)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']
