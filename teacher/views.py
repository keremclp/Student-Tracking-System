from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q

# FORMS
from teacher.forms import TeacherProfileModelForm, TeacherTimetableModelForm, TeacherCreateClassroom, CreateStudentClassroom

# MODELS
from classroom.models import Classroom, Timetable
from student.models import StudentClassroom, StudentProfile
from teacher.models import TeacherProfile


def teacher_dashboard(request):
    user = request.user
    
    try:
        teacher_profile = TeacherProfile.objects.get(user=user)
    except TeacherProfile.DoesNotExist:
        teacher_profile = None

    if teacher_profile:
        # Get the StudentClassrooms where the teacher is responsible
        responsible_classrooms = teacher_profile.studentclassroom_set.all()

        students_in_responsible_classes = []
        for classroom in responsible_classrooms:
            # Get the students associated with each classroom
            students = classroom.students.all()
            students_in_responsible_classes.extend(students)

        context = dict(
            teacher_profile = teacher_profile,
            students_in_responsible_classes = students_in_responsible_classes
        )

        return render(request, 'teacher/teacher_dashboard.html', context)
    else:
        # Handle the case where the user is not associated with a TeacherProfile
        # You can return an error message or redirect them as needed.
        pass
    
    
    return render(request, 'teacher/teacher_dashboard.html', context)


def teacher_profile_overview(request, user_slug):
    teacher_profile = get_object_or_404(TeacherProfile, slug=user_slug)
    context = dict(
        teacher_profile=teacher_profile,
    )
    return render(request, 'teacher/teacher_profile/teacher_profile_overview.html', context)


def teacher_profile_edit(request, user_slug):
    user = request.user
    profile = get_object_or_404(TeacherProfile, slug=user_slug)
    initial_data = dict(
        first_name=user.first_name,
        last_name=user.last_name,
    )
    form = TeacherProfileModelForm(instance=profile, initial=initial_data)
    if request.method == "POST":
        form = TeacherProfileModelForm(
            request.POST or None,
            request.FILES or None,
            instance=profile
        )
        if form.is_valid():
            f = form.save(commit=False)
            print(form.cleaned_data)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            new_profile_image = form.cleaned_data.get('profile_image')
            if new_profile_image:
                user.profile_image = new_profile_image
                user.save()

            user.save()
            profile.save()
            f.save()
            return redirect('teacher:teacher_profile_overview', user_slug=user_slug)

    context = dict(
        form=form,
        title="Edit Profile",
        profile=profile,

    )
    return render(request, 'student/student_profile/student_profile_settings.html', context)

# TODO: for create-timetable add editing if teacher add wrong timetable


def teacher_create_timetable(request):
    form = TeacherTimetableModelForm()
    if request.method == "POST":
        form = TeacherTimetableModelForm(request.POST)
        if form.is_valid():

            # find the logged user in TeacherProfile model
            teacher_profile = get_object_or_404(
                TeacherProfile, user=request.user)
            form.instance.teacher = teacher_profile
            form.save()
            return redirect('teacher:teacher_dashboard')
    context = dict(
        form=form,
        title="Create Timetable",
    )
    return render(request, 'teacher/teacher_create_timetable.html', context)


def teacher_create_classroom(request):
    form = TeacherCreateClassroom()
    if request.method == "POST":
        form = TeacherCreateClassroom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            grade_level = form.cleaned_data['grade_level']
            if Classroom.objects.filter(name=name, grade_level=grade_level).exists():
                context = dict(
                    form=form,
                    title='Create Classroom'
                )
                return render(request, 'teacher/teacher_classroom_create.html', context)
            else:
                form.save()
                return redirect('teacher:teacher_dashboard')
    context = dict(
        form=form,
        title="Create Classroom",
    )
    return render(request, 'teacher/teacher_classroom_create.html', context)



def add_student_classroom(request):
    form = CreateStudentClassroom()
    if request.method == "POST":
        form = CreateStudentClassroom(request.POST)
        if form.is_valid():
            classroom = form.cleaned_data['classroom']
            students = form.cleaned_data['students']

            # Check if a StudentClassroom already exists for this classroom
            student_classroom, created = StudentClassroom.objects.get_or_create(classroom=classroom)

            # Check if the selected students are already associated with the classroom
            existing_students = student_classroom.students.all()
            new_students = set(students) - set(existing_students)

            if not new_students:
                print('These students are already in the classroom.')
                return redirect('teacher:teacher_dashboard')

            # Add new students to the existing classroom
            student_classroom.students.add(*new_students)

            # Save the StudentClassroom object
            student_classroom.save()

            teacher_profile = get_object_or_404(TeacherProfile, user=request.user)
            student_classroom.responsible_teacher = teacher_profile
            student_classroom.save()

            return redirect('teacher:teacher_dashboard')

    context = dict(
        form=form,
        title="Add Students to Classroom",
    )
    return render(request, 'teacher/teacher_classroom_create.html', context)



def activate_student(request, student_id):
    # Ensure that only teachers can activate students (you can modify this logic)
    if not request.user.role == 'teacher':
        return redirect('teacher_dashboard')

    student = get_object_or_404(StudentProfile, id=student_id)

    # Activate the student
    student.phone_number_active = True
    student.save()

    # Optionally, change the status from "not verified" to "verified"
    # You need to define the appropriate field in your StudentProfile model for this status.

    return redirect('teacher:teacher_dashboard')
