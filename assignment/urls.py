from django.urls import path
from .views import create_quiz, quiz_detail, solve_quiz, quiz_results, create_questions, solve_quiz_lists
app_name = 'assignment'
urlpatterns = [
    path('create-quiz/', create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),
    path('solve_quiz/<int:quiz_id>/', solve_quiz, name='solve_quiz'),
    path('quiz_results/<int:quiz_id>/<slug:student_slug>', quiz_results, name='quiz_results'),
    path('create_questions/', create_questions, name='create_questions'),
    path('quiz-lists/', solve_quiz_lists, name='solve_quiz_lists'),
]
