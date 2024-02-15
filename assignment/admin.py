from django.contrib import admin
from assignment.models import Question,Quiz,Choice,Result, UserAnswer, SolvedQuiz
# Register your models here.

admin.site.register(Question)
admin.site.register(Result)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'question',
        'choice',
        'student'
    )
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'text',
        'is_correct',
    )
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'title',
    )

@admin.register(SolvedQuiz)

class SolvedQuizAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'quiz',
        'student'
    )