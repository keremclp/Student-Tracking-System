from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import AssignmentForm, ChoiceFormSet, QuizForm, QuestionForm, UploadedSolutionForm
from django.contrib.auth.decorators import login_required

from assignment.models import AssignmentFile, Quiz, Choice, Result, SolvedQuiz, UserAnswer
from teacher.models import TeacherProfile
from student.models import StudentProfile
from django.http import HttpResponse

from django.core.exceptions import ValidationError
from assignment.validation import validate_quiz_id, validate_student_slug


@login_required(login_url='account:error_view')
def create_quiz(request):
    if request.user.role == 'teacher':
        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                teacher_profile = get_object_or_404(
                    TeacherProfile, user=request.user)
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
            for i in range(0, upper_bound):
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
    questions = quiz.question_set.all()  # type: ignore
    return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})


@login_required(login_url='account:error_view')
def solve_quiz(request, quiz_id):
    user = request.user
    student_profile = get_object_or_404(StudentProfile, user=user)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()  # type: ignore
    questions_choices = [(question, question.choice_set.all())
                         for question in questions]
    # print(questions_choices)
    # Check if the user has already solved the quiz
    result_exists = Result.objects.filter(
        student=student_profile, quiz=quiz).exists()
    if result_exists:
        messages.info(request, f'You have already solved {quiz.title}')
        return redirect('assignment:quiz_results', quiz_id=quiz.pk, student_slug=student_profile.slug)

    if request.method == 'POST':
        print(request.POST)
        score = 0
        for i, question in enumerate(questions, 1):
            selected_choice = request.POST.get(f'question{i}')
            print(selected_choice)
            if selected_choice:
                print("--------------------before choice")
                choice = question.choice_set.get(id=int(selected_choice))
                # save the user answer on model UserAnswer
                # Assuming the user's answer is sent in the request.POST data
                user_choice = Choice.objects.get(id=selected_choice)
                # Create and save the UserAnswer

                user_answer = UserAnswer(
                    question=question, choice=user_choice, student=student_profile)
                user_answer.save()
                if choice.is_correct:
                    score += question.score
                print("after choice--------------------")
                # if choice.is_correct:
                #     score += 1

        if request.user.role == 'student':
            # Save the quiz into the SolvedQuiz model
            solved_quiz = SolvedQuiz(
                quiz=quiz, student=student_profile, score=score)
            solved_quiz.save()
            result, created = Result.objects.get_or_create(
                student=student_profile, quiz=quiz, score=score)
            if created:
                result.save()
            return redirect('assignment:quiz_results', quiz_id=quiz.pk, student_slug=student_profile.slug)

    include_input = True
    context = dict(
        quiz=quiz,
        questions=questions,
        questions_choices=questions_choices,
        include_input=include_input
    )

    return render(request, 'assignment/solve_quiz.html', context)


def quiz_results(request, quiz_id, student_slug):
    """View function to show the results of a quiz."""
    try:
        validate_quiz_id(quiz_id)
        validate_student_slug(student_slug)
    except ValidationError as e:
        return redirect("account:error_view")

    student = get_object_or_404(StudentProfile, slug=student_slug)
    quiz = Quiz.objects.get(id=quiz_id)
    result = get_object_or_404(Result, quiz=quiz, student=student)
    print("Result", result)
    user_answers = UserAnswer.objects.filter(student=student)
    questions_choices = [(answer.question, answer.choice)
                         for answer in user_answers]

    print(questions_choices)

    include_input = False
    context = dict(
        quiz=quiz,
        result=result,
        questions_choices=questions_choices,
        include_input=include_input
    )
    return render(request, 'assignment/quiz_results.html', context)


def solve_quiz_lists(request):
    """View function to show the results of a quiz."""
    student = get_object_or_404(StudentProfile, user=request.user)
    quizzes = Quiz.objects.all()
    solved_quizes = SolvedQuiz.objects.filter(student=student)

    context = dict(
        quizzes=quizzes,
        solved_quizes=solved_quizes
    )
    return render(request, 'assignment/solve_quiz_lists.html', context)


# ASSIGNMENT VIA UPLOADING FILE
def create_assignment(request):
    user = request.user
    teacher_profile = get_object_or_404(TeacherProfile, user=user)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.teacher = teacher_profile
            assignment.save()
    else:
        form = AssignmentForm()
    return render(request, 'assignment/create_assignment.html', {'form': form})


@login_required(login_url='account:error_view')
def upload_solution(request, assignment_id):
    student = get_object_or_404(StudentProfile, user=request.user)
    assignment = AssignmentFile.objects.get(pk=assignment_id)
    if request.user.role == 'teacher':
        return redirect('teacher:teacher_dashboard')
    if request.method == 'POST':
        form = UploadedSolutionForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.student = student
            solution.assignment = assignment
            solution.save()
    else:
        form = UploadedSolutionForm()
    return render(request, 'assignment/upload_solution.html', {'form': form, 'assignment': assignment})
