from django.shortcuts import get_object_or_404, render, redirect
from .forms import ChoiceFormSet, QuizForm, QuestionForm

from assignment.models import Quiz, Question, Choice, Result
from teacher.models import TeacherProfile

def create_quiz(request):
    if request.user.is_authenticated and request.user.role =='teacher':
        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                teacher_profile = get_object_or_404(TeacherProfile, user=request.user)
                quiz = form.save(commit=False)
                quiz.teacher = teacher_profile
                quiz.save()
                return redirect('teacher:teacher_dashboard')
        else:
            form = QuizForm()
        return render(request, 'assignment/create_quiz.html', {'form': form})
    else:
        return redirect('account:login_view')  # or handle permission denied

def create_questions(request):
    if request.method == 'POST':
        print(request.POST)
        question_form = QuestionForm(request.POST)
        choice_formset = ChoiceFormSet(request.POST)
        print(choice_formset)
        print("before if")
        if question_form.is_valid() and choice_formset.is_valid():
            # Save the quiz
            print("inside if")
            # Save the question associated with the quiz
            array = []
            question = question_form.save(commit=False)
            question.quiz.pk = request.POST.get('quiz')
            question.save()
            for i in range(0,5):
                choice = choice_formset.save(commit=False)
                array.append(choice)
                print(array[i])
                array[i][0].question = question
                array[i][0].text = request.POST.get(f'choice_set-{i}-question')
                array[i][0].save()
                
            

            # Redirect to a view that lists all quizzes
            return redirect('assignment:create_quiz')

    else:
        question_form = QuestionForm()
        choice_formset = ChoiceFormSet()

    context = {
        'title': 'Create Questions',
        'question_form': question_form,
        'choice_formset': choice_formset,
    }

    return render(request, 'assignment/create_questions.html', context)
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.question_set.all()
    return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})


def solve_quiz(request, quiz_id):
    def calculate_score(answers, questions):
        # Implement your scoring logic here
        score = 0
        for question in questions:
            if question.correct_choice == answers.get(str(question.id)):
                score += 1
        return score

    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        # Handle submitted answers
        form = AnswerForm(request.POST)
        if form.is_valid():
            # Process the answers and calculate the score
            score = calculate_score(form.cleaned_data, questions)
            # Save the result
            Result.objects.create(
                student=request.user.student, quiz=quiz, score=score)
            return redirect('quiz_results', quiz_id=quiz.pk)
    else:
        form = AnswerForm()

    return render(request, 'assignment/solve_quiz.html', {'quiz': quiz, 'questions': questions, 'form': form})


def quiz_results(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    results = Result.objects.filter(quiz=quiz)
    return render(request, 'quiz_results.html', {'quiz': quiz, 'results': results})
