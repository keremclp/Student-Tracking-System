from django.shortcuts import get_object_or_404, render, redirect
from .forms import ChoiceFormSet, QuizForm, QuestionForm

from assignment.models import Quiz, Question, Choice, Result
from teacher.models import TeacherProfile
from student.models import StudentProfile

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
        print("before if")
        if question_form.is_valid() and choice_formset.is_valid():
            # Save the quiz
            print("inside if")
            # Save the question associated with the quiz
            
            question = question_form.save(commit=False)
            question.quiz.pk = request.POST.get('quiz')
            question.save()
            choice = choice_formset.save(commit=False)
            upper_bound = int(request.POST.get('choice_set-TOTAL_FORMS'))
            print(choice)
            # TODO: kullanıcı boş gönderdiği zaman hata alıyoruz!!
            for i in range(0,upper_bound):
                choice[i].question = question
                choice[i].text = request.POST.get(f'choice_set-{i}-text')
                choice[i].save()
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
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()
    questions_choices = [(question, question.choice_set.all())
                         for question in questions]
    # print(questions_choices)

    if request.method == 'POST':
        print(request.POST)
        score = 0 
        for i,question in enumerate(questions,1):
            selected_choice = request.POST.get(f'question{i}')
            print(selected_choice)
            if selected_choice:
                print("--------------------before choice")
                choice = question.choice_set.get(id=int(selected_choice))
                if choice.is_correct:
                    score += 1
                print("after choice--------------------")
                # if choice.is_correct:
                #     score += 1
        print(score)
        user = request.user
        student_profile = get_object_or_404(StudentProfile, user=user)
        if request.user.role == 'student':
            result = Result.objects.create(student=student_profile, quiz=quiz, score=score)
            return redirect('assignment:quiz_results', quiz_id=quiz.pk)
        # score = 0
        # for question in questions:
        #     selected_choice = request.POST.get(f'question-{question.id}')
        #     print(selected_choice)
        #     if selected_choice:
        #         choice = question.choice_set.get(id=int(selected_choice))
        #         if choice.is_correct:
        #             score += 1
        # print(score)
        # result = Result.objects.create(
        #     student=request.user.studentprofile, quiz=quiz, score=score)
        # return redirect('assignment:quiz_results', quiz_id=quiz.pk)

    context = dict(
        quiz=quiz,
        questions = questions, 
        questions_choices=questions_choices,
    )

    return render(request, 'assignment/solve_quiz.html', context)


def quiz_results(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    results = Result.objects.filter(quiz=quiz)
    return render(request, 'assignment/quiz_results.html', {'quiz': quiz, 'results': results})
