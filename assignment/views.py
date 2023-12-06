from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ChoiceFormSet, QuizForm, QuestionForm
from django.contrib.auth.decorators import login_required

from assignment.models import Quiz, Question, Choice, Result, UserAnswer
from teacher.models import TeacherProfile
from student.models import StudentProfile
from django.http import HttpResponse    


@login_required(login_url='account:error_view')
def create_quiz(request):
    if request.user.role =='teacher':
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
    return HttpResponse()  # Add a default return statement

    
@login_required(login_url='account:error_view')
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
            question.quiz.pk = question_form.cleaned_data['quiz']
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
    questions = quiz.question_set.all() # type: ignore
    return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})


@login_required(login_url='account:error_view')
def solve_quiz(request, quiz_id):
    user = request.user
    student_profile = get_object_or_404(StudentProfile, user=user)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all() # type: ignore
    questions_choices = [(question, question.choice_set.all())
                         for question in questions]
    # print(questions_choices)
    # Check if the user has already solved the quiz
    result_exists = Result.objects.filter(student=student_profile, quiz=quiz).exists()
    if result_exists:
        messages.info(request, f'You have already solved {quiz.title}')
        return redirect('assignment:quiz_results', quiz_id=quiz.pk, student_slug=student_profile.slug)

    if request.method == 'POST':
        print(request.POST)
        score = 0 
        for i,question in enumerate(questions,1):
            selected_choice = request.POST.get(f'question{i}')
            print(selected_choice)
            if selected_choice:
                print("--------------------before choice")
                choice = question.choice_set.get(id=int(selected_choice))
                # save the user answer on model UserAnswer
                for question in questions:
                    # Assuming the user's answer is sent in the request.POST data                    
                    user_choice = Choice.objects.get(id=selected_choice)
                    # Create and save the UserAnswer
                    user_answer = UserAnswer(question=question, choice=user_choice)
                    user_answer.save()
                if choice.is_correct:
                    score += 1
                print("after choice--------------------")
                # if choice.is_correct:
                #     score += 1

        if request.user.role == 'student' :
            result,created = Result.objects.get_or_create(student=student_profile, quiz=quiz, score=score)
            if created :
                result.save()
            return redirect('assignment:quiz_results', quiz_id=quiz.pk, student_slug= student_profile.slug)

    context = dict(
        quiz=quiz,
        questions = questions, 
        questions_choices=questions_choices,
    )

    return render(request, 'assignment/solve_quiz.html', context)


def quiz_results(request, quiz_id, student_slug):
    """View function to show the results of a quiz."""
    student = get_object_or_404(StudentProfile, slug=student_slug)
    quiz = Quiz.objects.get(id=quiz_id)
    result = get_object_or_404(Result, quiz=quiz, student=student)
    print(result.student)
    questions = quiz.question_set.all() # type: ignore 
    choices = Choice.objects.filter(question__in=questions, is_correct=True).order_by('question__id')
    print(choices)
    context = dict(
        quiz=quiz,
        result=result,
        questions=questions,
    )
    return render(request, 'assignment/quiz_results.html',context)
