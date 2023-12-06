from django.contrib import admin
from assignment.models import Question,Quiz,Choice,Result, UserAnswer
# Register your models here.

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Result)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'question',
        'choice',
    )
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'text',
        'is_correct',
    )
