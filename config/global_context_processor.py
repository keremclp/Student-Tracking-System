from student.models import StudentProfile

def profile_global(request):
    user = request.user
    print(user)
    # bring me profile 
    profile = StudentProfile.objects.get(user=user)
    return {'profile_global': profile}

def profile_image(request):
    user = request.user
    if user.is_authenticated and user.role == 'student':
        try:
            student_profile = StudentProfile.objects.get(user=user)
            profile_image_path = student_profile.user.profile_image.url
        except StudentProfile.DoesNotExist:
            profile_image_path = 'default_image_path'
    # elif user.is_authenticated and user.role == 'teacher': 
    #     try:
    #         student_profile = StudentProfile.objects.get(user=user)
    #         profile_image_path = student_profile.user.profile_image.url
    #     except StudentProfile.DoesNotExist:
    #         profile_image_path = 'default_image_path'
    else:
        profile_image_path = 'default_image_path'

    return {'profile_image': profile_image_path}
