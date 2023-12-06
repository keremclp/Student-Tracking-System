from django.contrib import admin
from assignment.models import Question,Quiz,Choice,Result, UserAnswer
# Register your models here.

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Choice)
admin.site.register(Result)
admin.site.register(UserAnswer)