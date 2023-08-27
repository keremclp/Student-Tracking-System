from student.models import StudentProfile

def profile_global(request):
    user = request.user
    print(user)
    # bring me profile 
    profile = StudentProfile.objects.get(user=user)
    return {'profile_global': profile}

def profile_image(request):
    user = request.user
    profile_image_path = 'default_image_path'
    profile_global = None
    
    if user.is_authenticated:
        if user.role == 'student':
            try:
                profile_student = StudentProfile.objects.get(user=user)
                profile_image_path = profile_student.user.profile_image.url
                profile_global = profile_student
            except StudentProfile.DoesNotExist:
                pass  # No need to change profile_image_path or profile_global

        # elif user.role == 'parent':
        #     try:
        #         profile_parent = ParentProfile.objects.get(user=user)
        #         profile_image_path = profile_parent.user.profile_image.url
        #         profile_global = profile_parent
        #     except ParentProfile.DoesNotExist:
        #         pass  # No need to change profile_image_path or profile_global

        # elif user.role == 'teacher':
        #     try:
        #         profile_teacher = TeacherProfile.objects.get(user=user)
        #         profile_image_path = profile_teacher.user.profile_image.url
        #         profile_global = profile_teacher
        #     except TeacherProfile.DoesNotExist:
        #         pass  # No need to change profile_image_path or profile_global

    return {
        'profile_image': profile_image_path,
        'profile_global': profile_global
    }



# elif user.is_authenticated and user.role == 'teacher': 
    #     try:
    #         student_profile = StudentProfile.objects.get(user=user)
    #         profile_image_path = student_profile.user.profile_image.url
    #     except StudentProfile.DoesNotExist:
    #         profile_image_path = 'default_image_path'


def completion_percentage(request):
    user = request.user 
    profile = StudentProfile.objects.get(user=user)
    total_fields = 4
    completed_fields = sum(
        field is not None and field != ""
        for field in [profile.birth_date, profile.bio, profile.phone_number, profile.address]
    )
    completion_percentage = (completed_fields / total_fields) * 100  
    return {'completion_percentage': completion_percentage}